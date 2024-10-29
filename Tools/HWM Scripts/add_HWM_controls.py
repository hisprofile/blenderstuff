'''

README!!!

This script will apply HWM controls to models *MEANT* for HWM controls. Ideally, the head should be its own mesh
for best performance.

You know a model is HWM if it has shapekeys named "BrowOutV", "SmileFull" or "PuffLipsLo". If shapekeys
like these cannot be found, you likely do not have an HWM model. Apologies.

This script requires two vertex groups, "blendright" and "blendleft". blendright should be a gradient starting
from the right side of the face towards the left, and vice versa, made possible using the Gradient tool
in "Weight Paint" mode. You can enable "wireframe" in the object tab to help guide yourself for an equal fade.
The fading should start near the corners of the lips, maybe a little more out.

This script will also add Wrinkle Maps for use in the Shader editor, accessible through the "tension" attribute.
The X/Red channel is compress, Y/Green is stretch. In order for wrinkles to be performed, SetWrinkleScale functions
need to be written in the "LUA PARAMETERS" section of the script. By default, it is included. If your model does not
have wrinkle maps, set "final_do_wrinkles" to False.

This script uses default .lua script functions, used generally for all the TF2 mercs. If your model does not
work as expected, it's possible you may need to ask for the creator's .lua script.


Written by hisanimations

'''

final_do_wrinkles = True

import bpy
from collections import defaultdict
import json
from string import ascii_lowercase as letters
import numpy as np

C = bpy.context
obj = C.object
data = obj.data

true = True
false = False

left_group = obj.vertex_groups.get('blendleft')
right_group = obj.vertex_groups.get('blendright')

if None in {left_group, right_group}:
    print('''!!!
You are missing "blendleft" and "blendright" vertex groups!
!!!''')

vertices = len(data.vertices)

group_controls = defaultdict(list)
eyelids = dict()
stereos = dict()
dominations = dict()
ranges = dict()
stereo_set = set()
slider_list = list()
flex_set = set()

shapes = list()

do_wrinkles = False

for attr in filter(lambda a: getattr(a, 'name', '').startswith('SK.'), data.attributes):
    if '_' in attr.name: continue
    flex_set.add(attr.name[3:])
    
is_multi = dict()

class null:
    weight = 0.0
    
def only(item, *argv):
    for arg in argv:
        if arg != item:
            return False
    return True

def GroupControls(name, *argv):
    
    '''
    
    "name" declares a control, slider, or flex controller.
    If a slider or name is not mentioned here, assume a shape key exists with the same name,
    and its range is 0..1.
    A slider will be created to drive only that shapekey.
    
    If a slider has two shapekeys, then its range will be -1..1.
    It will have the first shapekey blend in when the slider is -1
    and the second shapekey blend in when the slider is 1
    
    
    This behavior is switched when the slider is ran through SetEyelidControl.
    In which case, the range remains but the value is mapped to 0..1.
    A new slider named "multi_{name}" will be created with a range of -1..1.
    Its value will also be mapped to 0..1 and be used in a mixing function,
        where "multi_{name}" will be used as a factor to mix between shapekey one and shapekey two.
    For example, if "multi_{name}" is zero, shapekey one will be 1.0. If the factor is
        0.5, shapekey one and shapekey two will equally be 0.5. If 1.0, shapekey two is 1.0.
        
    If a slider has three shapekeys, a "multi" slider will also be created to mix between these three shapekeys.
    As for the mixing, shapekey one will be 1.0 if "multi" is -1.0.
        shapekey two will be 1.0 if "multi" is 0.0.
        shapekey three will be 1.0 if "multi" is 1.0.
    Their final values are multiplied by the slider value.
    
    Shapekeys who's names consist of other shapekeys joined by underscores fade in when
    all mentioned shape keys are activated. These are called corrective shapekeys.
    Their final value is the product of all values of mentioned shape keys.
    
    '''
    
    for arg in argv:
        group_controls[name].append(arg)
        flex_set.add(arg)
    if len(argv) == 2:
        ranges[name] = (-1, 1)
    if len(argv) > 2:
        #ranges[name] = (0, 1)
        is_multi[name] = True
        
# reorder controls
def ReorderControls(*argv):
    for arg in argv:
        slider_list.append(arg)
        if group_controls.get(arg) == None:
            flex_set.add(arg)
        
def SetEyelidControl(name, state):
    if state == False: return
    is_multi[name] = True
    eyelids[name] = True

# setup stereo controls
def SetStereoControl(name, state):
    if state == False: return
    stereos[name] = True
    if not group_controls.get(name):
        stereo_set.add(name)
        return
    for i in group_controls[name]:
        stereo_set.add(i)
        
def SetWrinkleScale(name, shape, mult):
    global do_wrinkles
    do_wrinkles = True
    bak = mult
    if bak == 0:
        return None
    if bak > 0:
        bak = 1
    else:
        bak = -1
    method = "C" if mult < 0 else "S"
    print(mult)
    if stereos.get(name) == True: # if split
        item = ".".join(["WR", shape+"R", method])
        shapes.append((shape+"R", item, bak, mult))
        #bpy.context.object.data['scales'][item] = mult
        item = ".".join(["WR", shape+"L", method])
        shapes.append((shape+"L", item, bak, mult))
        #bpy.context.object.data['scales'][item] = mult
    else:
        item = ".".join(["WR", shape, method])
        shapes.append((shape, item, bak, mult))
        #bpy.context.object.data['scales'][item] = mult
        
dominators = dict()
suppressed = defaultdict(list)
hierarchy = defaultdict(list)
hierarchy_list = list()
hierarchy_inverse = dict()

'''

The final value of a set of dominators is determined by multiplying the value of each dominator with each other.
Then, the value will be remapped from 0..1 to 1..0. ( 1-final_value )

All dominators listed to suppress a shapekey will have their final values multiplied against each other.
The product will then be multiplied against the shapekey.

'''
# add control dominators
def AddDominationRule(winners, losers):
    winners = list(winners)
    losers = list(losers)
    #for loser in losers:
    #    for winner in winners:
    suppressed[losers[0]].append(winners)
    
''' START OF LUA PARAMETERS '''

funcs = '''

GroupControls( "CloseLid", "CloseLidLo", "CloseLidUp" );
GroupControls( "BrowInV", "WrinkleNose", "RaiseBrowIn" );
GroupControls( "NoseV", "PressNose", "SneerNose" );
GroupControls( "NostrilFlare", "SuckNostril", "BlowNostril" );
GroupControls( "CheekH", "DeflateCheek", "InflateCheek" );
GroupControls( "JawD", "SuckJaw", "JutJaw" );
GroupControls( "JawH", "SlideJawR", "SlideJawL" );
GroupControls( "JawV", "ClenchJaw", "OpenJaw" );
GroupControls( "LipsV", "CompressLips", "OpenLips" );
GroupControls( "LipUpV", "JutUpperLip", "OpenUpperLip" );
GroupControls( "LipLoV", "RaiseChin", "OpenLowerLip" );
GroupControls( "Smile", "SmileFlat", "SmileFull", "SmileSharp" );
GroupControls( "FoldLipUp", "SuckLipUp", "FunnelLipUp" );
GroupControls( "FoldLipLo", "SuckLipLo", "FunnelLipLo" );
GroupControls( "ScalpD", "ScalpBack", "ScalpForward" );
GroupControls( "TongueH", "TongueLeft", "TongueRight" );
GroupControls( "TongueCurl", "TongueCurlUp", "TongueCurlDown" );
GroupControls( "TongueD", "TongueBack", "TongueOut" );
GroupControls( "TongueWidth", "TongueNarrow", "TongueWide" );
        
ReorderControls(
    "CloseLid", 
    "InnerSquint", 
    "OuterSquint", 
    "BrowInV", 
    "BrowOutV", 
    "Frown", 
    "NoseV", 
    "NostrilFlare", 
    "CheekV", 
    "CheekH", 
    "JawD", 
    "JawH", 
    "JawV", 
    "LipsV", 
    "LipUpV", 
    "LipLoV", 
    "Smile", 
    "Platysmus", 
    "FoldLipUp", 
    "FoldLipLo", 
    "PuckerLipUp", 
    "PuckerLipLo", 
    "LipCnrTwst", 
    "Dimple", 
    "PuffLipUp", 
    "PuffLipLo", 
    "ScalpD", 
    "TongueD", 
    "TongueH", 
    "TongueV", 
    "TongueCurl", 
    "TongueFunnel", 
    "TongueWidth",
);

SetEyelidControl("CloseLid", true );

SetStereoControl("CloseLid", true );
SetStereoControl("InnerSquint", true );
SetStereoControl("OuterSquint", true );
SetStereoControl("BrowInV", true );
SetStereoControl("BrowOutV", true );
SetStereoControl("Frown", true );
SetStereoControl("NoseV", true );
SetStereoControl("NostrilFlare", true );
SetStereoControl("CheekV", true );
SetStereoControl("CheekH", true );
SetStereoControl("JawD", false );
SetStereoControl("JawH", false );
SetStereoControl("JawV", false );
SetStereoControl("LipsV", true );
SetStereoControl("LipUpV", true );
SetStereoControl("LipLoV", true );
SetStereoControl("Smile", true );
SetStereoControl("Platysmus", true );
SetStereoControl("FoldLipUp", true );
SetStereoControl("FoldLipLo", true );
SetStereoControl("PuckerLipUp", true );
SetStereoControl("PuckerLipLo", true );
SetStereoControl("LipCnrTwst", true );
SetStereoControl("Dimple", true );
SetStereoControl("PuffLipUp", true );
SetStereoControl("PuffLipLo", true );
SetStereoControl("ScalpD", true );
SetStereoControl("hideCig", false );
SetStereoControl("TongueV", false );
SetStereoControl("TongueH", false );
SetStereoControl("TongueCurl", false );
SetStereoControl("TongueD", false );
        
AddDominationRule( { "BrowOutV" }, { "WrinkleNose"} );
AddDominationRule( { "FunnelLipLo" }, { "PuffLipLo"} );
AddDominationRule( { "FunnelLipLo" }, { "PuffLipUp"} );
AddDominationRule( { "FunnelLipUp" }, { "PuffLipLo"} );
AddDominationRule( { "FunnelLipUp" }, { "PuffLipUp"} );
AddDominationRule( { "LipCnrTwst" }, { "Dimple"} );
AddDominationRule( { "OpenJaw" }, { "InflateCheek"} );
AddDominationRule( { "OpenLips" }, { "PuffLipLo"} );
AddDominationRule( { "OpenLips" }, { "PuffLipUp"} );
AddDominationRule( { "OpenLowerLip" }, { "CompressLips"} );
AddDominationRule( { "OpenLowerLip" }, { "FunnelLipLo"} );
AddDominationRule( { "OpenLowerLip" }, { "PuffLipLo"} );
AddDominationRule( { "OpenLowerLip" }, { "PuffLipUp"} );
AddDominationRule( { "OpenLowerLip", "OpenUpperLip" }, { "OpenLips"} );
AddDominationRule( { "OpenUpperLip" }, { "CompressLips"} );
AddDominationRule( { "OpenUpperLip" }, { "FunnelLipUp"} );
AddDominationRule( { "OpenUpperLip" }, { "PuffLipLo"} );
AddDominationRule( { "OpenUpperLip" }, { "PuffLipUp"} );
AddDominationRule( { "Platysmus" }, { "FunnelLipLo"} );
AddDominationRule( { "Platysmus" }, { "FunnelLipUp"} );
AddDominationRule( { "Platysmus" }, { "LipCnrTwst"} );
AddDominationRule( { "Platysmus" }, { "PuckerLipLo"} );
AddDominationRule( { "Platysmus" }, { "PuckerLipUp"} );
AddDominationRule( { "PuckerLipLo" }, { "SmileFlat"} );
AddDominationRule( { "PuckerLipLo" }, { "SmileFull"} );
AddDominationRule( { "PuckerLipLo" }, { "SmileSharp"} );
AddDominationRule( { "PuckerLipLo" }, { "SuckLipLo"} );
AddDominationRule( { "PuckerLipLo",	"OpenJaw" }, { "FunnelLipLo"} );
AddDominationRule( { "PuckerLipUp" }, { "SmileFlat"} );
AddDominationRule( { "PuckerLipUp" }, { "SmileFull"} );
AddDominationRule( { "PuckerLipUp" }, { "SmileSharp"} );
AddDominationRule( { "PuckerLipUp" }, { "SuckLipUp"} );
AddDominationRule( { "PuckerLipUp", "OpenJaw" }, { "FunnelLipUp"} );
AddDominationRule( { "SmileFull" }, { "InflateCheek"} );
AddDominationRule( { "SmileFull" }, { "SuckLipUp"} );

SetWrinkleScale( "CloseLid", "CloseLidLo", 0 )
SetWrinkleScale( "CloseLid", "CloseLidUp", 0 )
SetWrinkleScale( "ScalpD", "ScalpBack", 0 )
SetWrinkleScale( "ScalpD", "ScalpForward", 0 )
SetWrinkleScale( "BrowInV", "WrinkleNose", -0.5 )
SetWrinkleScale( "BrowInV", "RaiseBrowIn", 2 )
SetWrinkleScale( "NoseV", "PressNose", 1     )
SetWrinkleScale( "NoseV", "SneerNose", -1.25 )
SetWrinkleScale( "NostrilFlare", "SuckNostril", 0 )
SetWrinkleScale( "NostrilFlare", "BlowNostril", 0 )
SetWrinkleScale( "CheekH", "DeflateCheek", 0 )
SetWrinkleScale( "CheekH", "InflateCheek", 0 )
SetWrinkleScale( "JawD", "SuckJaw", 0 )
SetWrinkleScale( "JawD", "JutJaw", 0 )
SetWrinkleScale( "JawH", "SlideJawR", 0 )
SetWrinkleScale( "JawH", "SlideJawL", 0 )
SetWrinkleScale( "JawV", "ClenchJaw", 0 )
SetWrinkleScale( "JawV", "OpenJaw", 0 )
SetWrinkleScale( "LipsV", "CompressLips", 0 )
SetWrinkleScale( "LipsV", "OpenLips", 0 )
SetWrinkleScale( "LipUpV", "JutUpperLip", 0 )
SetWrinkleScale( "LipUpV", "OpenUpperLip", 0 )
SetWrinkleScale( "LipLoV", "RaiseChin", -0.75 )
SetWrinkleScale( "LipLoV", "OpenLowerLip", 0 )
SetWrinkleScale( "Smile", "SmileFlat", 1 )
SetWrinkleScale( "Smile", "SmileFull", 1 )
SetWrinkleScale( "Smile", "SmileSharp", 1 )
SetWrinkleScale( "FoldLipUp", "SuckLipUp", 0 )
SetWrinkleScale( "FoldLipUp", "FunnelLipUp", -0.75 )
SetWrinkleScale( "FoldLipLo", "SuckLipLo", 0 )
SetWrinkleScale( "FoldLipLo", "FunnelLipLo", -0.5 )
SetWrinkleScale( "TongueD", "TongueOut", 0 )
SetWrinkleScale( "TongueD", "TongueBack", 0 )
SetWrinkleScale( "TongueH", "TongueRight", 0 )
SetWrinkleScale( "TongueH", "TongueLeft", 0 )
SetWrinkleScale( "TongueCurl", "TongueCurlDown", 0 )
SetWrinkleScale( "TongueCurl", "TongueCurlUp", 0 )
SetWrinkleScale( "TongueWidth", "TongueNarrow", 0 )
SetWrinkleScale( "TongueWidth", "TongueWide", 0 )
SetWrinkleScale( "BrowOutV", "BrowOutV", 0.75 )
SetWrinkleScale( "Frown", "Frown", -1 )
SetWrinkleScale( "CheekV", "CheekV", -1 )
SetWrinkleScale( "Platysmus", "Platysmus", 2 )
SetWrinkleScale( "PuckerLipUp", "PuckerLipUp", -2 )
SetWrinkleScale( "PuckerLipLo", "PuckerLipLo", -1 )
SetWrinkleScale( "LipCnrTwst", "LipCnrTwst", 0 )
SetWrinkleScale( "Dimple", "Dimple", -2 )
SetWrinkleScale( "PuffLipUp", "PuffLipUp", 0 )
SetWrinkleScale( "PuffLipLo", "PuffLipLo", 0 )
SetWrinkleScale( "TongueV", "TongueV", 0 )
SetWrinkleScale( "TongueFunnel", "TongueFunnel", 0 )
SetWrinkleScale( "InnerSquint", "InnerSquint", -0.8 )
SetWrinkleScale( "OuterSquint", "OuterSquint", -1 )

'''.replace('--', '#')

''' END OF LUA PARAMETERS '''

exec(funcs)

roundto = 5
for flex in flex_set:
    level = len(suppressed.get(flex, []))
    hierarchy[level].append(flex)

for level, items in hierarchy.items():
    for item in items:
        hierarchy_inverse[item] = level

hierarchy_list = sorted(flex_set, key=lambda a: hierarchy_inverse.get(a, 0))

SK = data.shape_keys
KB = SK.key_blocks
#SK.animation_data_clear()
prop_list = ['aaa_fs']
flex_map = {'fs': 'aaa_fs'}

for key in list(KB):
    name = key.name
    if not len(stereo_set.intersection(set(name.split('_')))): continue
    print(name)
    if name.endswith('L'):
        key.vertex_group = 'blendleft'
        if KB.get(name[:-1]+'R'): continue
        new_key = obj.shape_key_add(name=name+'R', from_mix=False)
        zeros = np.zeros(vertices*3, np.float32)
        key.data.foreach_get('co', zeros)
        new_key.data.foreach_set('co', zeros)
        continue
    if name.endswith('R'):
        key.vertex_group = 'blendright'
        if KB.get(name[:-1]+'L'): continue
        new_key = obj.shape_key_add(name=name+'L', from_mix=False)
        zeros = np.zeros(vertices*3, np.float32)
        key.data.foreach_get('co', zeros)
        new_key.data.foreach_set('co', zeros)
        continue
    if name and only(None, KB.get(name+'L'), KB.get(name+'R')):
        key.name += 'L'
        new_key = obj.shape_key_add(name=name+'R', from_mix=False)
        zeros = np.zeros(vertices*3, np.float32)
        key.data.foreach_get('co', zeros)
        new_key.data.foreach_set('co', zeros)
        continue
    print(name, False)
data.update()
#assert False
for key, value in list(data.items()):
    if not isinstance(value, float): continue
    split = key.split('_', maxsplit=1)
    if len(split) < 2: continue
    num, name = split
    try:
        num = int(''.join(map(lambda x: str(letters.find(x)), num)))
    except ValueError: continue
    del data[key]
data['aaa_fs'] = 1.0
prop_count = iter(range(1, 10000))

def number_format(x):
    return ''.join(list(map(lambda a: letters[int(a)], ['0']*(3-len(str(x))) + list(str(x))))) + '_'

for slider in slider_list:
    if stereos.get(slider):
        right = number_format(next(prop_count)) + 'right_' + slider
        left = number_format(next(prop_count)) + 'left_' + slider
        
        flex_map['right_' + slider] = right
        flex_map['left_' + slider] = left
        
        data[right] = 0.0
        data[left] = 0.0
        
        count = len(group_controls.get(slider, []))
        if count == 2:
            data.id_properties_ui(right).update(min=-1.0, max=1.0)
            data.id_properties_ui(left).update(min=-1.0, max=1.0)
        else:
            data.id_properties_ui(right).update(min=.0, max=1.0)
            data.id_properties_ui(left).update(min=.0, max=1.0)
    else:
        main = number_format(next(prop_count)) + slider
        data[main] = 0.0
        flex_map[slider] = main
        
        count = len(group_controls.get(slider, []))
        if count == 2:
            data.id_properties_ui(main).update(min=-1.0, max=1.0)
        else:
            data.id_properties_ui(main).update(min=.0, max=1.0)
        
    if is_multi.get(slider):
        multi = number_format(next(prop_count)) + 'multi_' + slider
        data[multi] = 0.0
        flex_map['multi_'+slider] = multi
        data.id_properties_ui(multi).update(min=-1.0, max=1.0)
            
data['flexcontrollers'] = flex_map
data.update()
for key in KB:
    if not '_' in getattr(key, 'name', ''): continue
    key.driver_remove('value')
    driver = key.driver_add('value')
    driv = driver.driver
    
    expr = ''

    if key.name.endswith('R'):
        key.vertex_group = 'blendright'
        side = 'R'
        split = key.name[:-1].split('_')
        split = list(map(lambda a: (KB.get(a) or KB.get(a+side)), split))
        if None in split: continue
    elif key.name.endswith('L'):
        key.vertex_group = 'blendleft'
        side = 'L'
        split = key.name[:-1].split('_')
        split = list(map(lambda a: (KB.get(a) or KB.get(a+side)), split))
        if None in split: continue
    else:
        split = key.name.split('_')
        split = list(map(lambda a: KB.get(a), split))
        if None in split: continue
    
    for n, Var in enumerate(split):
        n = str(n)
        var = driv.variables.new()
        var.name = 'V'+n
        var.type = 'SINGLE_PROP'
        targ = var.targets[0]
        targ.id_type = 'KEY'
        targ.id = SK
        targ.data_path = Var.path_from_id('value')
        expr += f'*{var.name}'
    expr = expr[1:]
        
    var = driv.variables.new()
    var.name = 'FS'
    var.type = 'SINGLE_PROP'
    targ = var.targets[0]
    targ.id_type = 'MESH'
    targ.id = data
    targ.data_path = '["aaa_fs"]'
    #expr += f'*{var.name}'
    
    #driv.expression = expr
    driv.expression = f'({expr})/FS'
    
def applyDominationRules(driv, winners, append, *, sfx=''):
    for n, winner in enumerate(winners):
        n = str(n)
        if len(winner) == 1:
            winner = winner[0]
            var = driv.variables.new()
            var.name = 'D'+n
            var.type = 'SINGLE_PROP'
            targ = var.targets[0]
            targ.id_type = 'KEY'
            targ.id = SK
            targ.data_path = (KB.get(winner+sfx) or KB.get(winner)).path_from_id('value')
            
            append += f'*(1-{var.name})'
        else:
            for nn, winner2 in enumerate(winner):
                nn = str(nn)
                var = driv.variables.new()
                var.name = 'D'+n+nn
                var.type = 'SINGLE_PROP'
                targ = var.targets[0]
                targ.id_type = 'KEY'
                targ.id = SK
                targ.data_path = (KB.get(winner2+sfx) or KB.get(winner2)).path_from_id('value')
                
                append += f'*(1-{var.name})'
    return append

def repair_flex(flex):
    return False
    print(flex)
    print(KB.get(flex+'L'), KB.get(flex+'R'))
    if (found := KB.get(flex)) and only(None, KB.get(flex+'L'), KB.get(flex+'R')):
        print('case2!')
        found.name += 'L'
        new_key = obj.shape_key_add(name=flex+'R', from_mix=False)
        zeros = np.zeros(vertices*3, np.float32)
        found.data.foreach_get('co', zeros)
        new_key.data.foreach_set('co', zeros)
        return found
    if (found := KB.get(flex+'L')) and KB.get(flex+'R') == None:
        print('case!')
        new_key = obj.shape_key_add(name=flex+'R', from_mix=False)
        zeros = np.zeros(vertices*3, np.float32)
        found.data.foreach_get('co', zeros)
        new_key.data.foreach_set('co', zeros)
        return new_key
    if (found := KB.get(flex+'R')) and KB.get(flex+'L') == None:
        new_key = obj.shape_key_add(name=flex+'L', from_mix=False)
        zeros = np.zeros(vertices*3, np.float32)
        found.data.foreach_get('co', zeros)
        new_key.data.foreach_set('co', zeros)
        return new_key
    print('fail!')
    return False

for slider in slider_list:
    params = set()
    is_stereo = False
    has_multi = False
    if stereos.get(slider):
        is_stereo = True
        left = f'left_{slider}'
        right = f'right_{slider}'
        left_format = flex_map.get(left)
        right_format = flex_map.get(right)
        params.add(bool(flex_map.get(left)))
        params.add(bool(flex_map.get(right)))
    else:
        params.add(bool(flex_map.get(slider)))
    if is_multi.get(slider):
        has_multi = True
        multi = f'multi_{slider}'
        multi_format = flex_map.get(multi)
        params.add(bool(flex_map.get(multi)))
    if False in params:
        print(f'{slider} failed to verify!')
        continue
    controls = group_controls.get(slider, [])
    control_count = len(controls)
    slider_format = flex_map.get(slider)
    
    if (control_count == 2) and eyelids.get(slider):
        if is_stereo:
            for N, control in enumerate(group_controls[slider]):
                for sfx in ['L', 'R']:
                    key = KB.get(control+sfx)
                    if key == None:
                        if (key := repair_flex(control)) == False:
                            print(f'Failed to complete a pair for {control}!')
                            continue
                    
                    if sfx == 'L':
                        key.vertex_group = 'blendleft'
                    if sfx == 'R':
                        key.vertex_group = 'blendright'
                    
                    key.driver_remove('value')
                    driver = key.driver_add('value')
                    driv = driver.driver
                    
                    var = driv.variables.new()
                    var.name = 'MLT'
                    var.type = 'SINGLE_PROP'
                    targ = var.targets[0]
                    targ.id_type = 'MESH'
                    targ.id = data
                    targ.data_path = f'["{multi_format}"]'
                    
                    side = left_format if sfx == 'L' else right_format
                    
                    var = driv.variables.new()
                    var.name = 'V1'
                    var.type = 'SINGLE_PROP'
                    targ = var.targets[0]
                    targ.id_type = 'MESH'
                    targ.id = data
                    targ.data_path = f'["{side}"]'
                    
                    var = driv.variables.new()
                    var.name = 'FS'
                    var.type = 'SINGLE_PROP'
                    targ = var.targets[0]
                    targ.id_type = 'MESH'
                    targ.id = data
                    targ.data_path = '["aaa_fs"]'
                    
                    add = ''
                    
                    if winners := suppressed.get(control):
                        add += applyDominationRules(driv, winners, add, sfx=sfx)
                    #add += '*FS'
                    
                    if N == 0:
                        #driv.expression = '((MLT+1)/2)*((V1+1)/2)'#+add
                        driv.expression = f'min(max(((MLT+1)/2)*((V1+1)/2){add}, 0), 1)*FS'#+add
                    if N == 1:
                        #driv.expression = '((MLT-1)/-2)*((V1+1)/2)'+add
                        driv.expression = f'min(max(((MLT-1)/-2)*((V1+1)/2){add}, 0), 1)*FS'
                        
    elif control_count == 2:
        if is_stereo:
            for N, control in enumerate(group_controls[slider]):
                for sfx in ['L', 'R']:
                    key = KB.get(control+sfx)
                    if key == None:
                        if (key := repair_flex(control)) == False:
                            print(f'Failed to complete a pair for {control}!')
                            continue
                    if sfx == 'L':
                        key.vertex_group = 'blendleft'
                    if sfx == 'R':
                        key.vertex_group = 'blendright'
                    key.driver_remove('value')
                    driver = key.driver_add('value')
                    driv = driver.driver
                    
                    side = left_format if sfx == 'L' else right_format
                    
                    var = driv.variables.new()
                    var.name = 'V1'
                    var.type = 'SINGLE_PROP'
                    targ = var.targets[0]
                    targ.id_type = 'MESH'
                    targ.id = data
                    targ.data_path = f'["{side}"]'
                    
                    var = driv.variables.new()
                    var.name = 'FS'
                    var.type = 'SINGLE_PROP'
                    targ = var.targets[0]
                    targ.id_type = 'MESH'
                    targ.id = data
                    targ.data_path = '["aaa_fs"]'
                    
                    add = ''
                    if winners := suppressed.get(control):
                        add += applyDominationRules(driv, winners, add, sfx=sfx)
                    print(control, add == '')
                    #add += '*FS'
                    
                    if N == 0:
                        #driv.expression = 'min(max(V1*-1, 0), 1)'+add
                        driv.expression = f'min(max(min(max(V1*-1, 0), 1){add}, 0), 1)*FS'
                    if N == 1:
                        driv.expression = f'min(max(min(max(V1, 0), 1){add}, 0), 1)*FS'#+add
        else:
            for N, control in enumerate(group_controls[slider]):
                key = KB.get(control)
                if key == None: continue
                key.driver_remove('value')
                driver = key.driver_add('value')
                driv = driver.driver
                
                var = driv.variables.new()
                var.name = 'V1'
                var.type = 'SINGLE_PROP'
                targ = var.targets[0]
                targ.id_type = 'MESH'
                targ.id = data
                targ.data_path = f'["{slider_format}"]'
                
                var = driv.variables.new()
                var.name = 'FS'
                var.type = 'SINGLE_PROP'
                targ = var.targets[0]
                targ.id_type = 'MESH'
                targ.id = data
                targ.data_path = '["aaa_fs"]'
                
                add = ''
                if winners := suppressed.get(control):
                    add += applyDominationRules(driv, winners, add)
                #add += '*FS'
                
                if N == 0:
                    #driv.expression = 'min(max(V1*-1, 0), 1)'+add
                    driv.expression = f'min(max(min(max(V1*-1, 0), 1){add}, 0), 1)*FS'
                if N == 1:
                    #driv.expression = 'min(max(V1*1, 0), 1)'+add
                    driv.expression = f'min(max(min(max(V1, 0), 1){add}, 0), 1)*FS'
    elif control_count == 3:
        if is_stereo:
            for N, control in enumerate(group_controls[slider]):
                for sfx in ['L', 'R']:
                    key = KB.get(control+sfx)
                    if key == None:
                        if (key := repair_flex(control)) == False:
                            print(f'Failed to complete a pair for {control}!')
                            continue
                
                    if sfx == 'L':
                        key.vertex_group = 'blendleft'
                    if sfx == 'R':
                        key.vertex_group = 'blendright'
                    
                    key.driver_remove('value')
                    driver = key.driver_add('value')
                    driv = driver.driver
                    
                    var = driv.variables.new()
                    var.name = 'MLT'
                    var.type = 'SINGLE_PROP'
                    targ = var.targets[0]
                    targ.id_type = 'MESH'
                    targ.id = data
                    targ.data_path = f'["{multi_format}"]'
                    
                    side = left_format if sfx == 'L' else right_format
                    
                    var = driv.variables.new()
                    var.name = 'V1'
                    var.type = 'SINGLE_PROP'
                    targ = var.targets[0]
                    targ.id_type = 'MESH'
                    targ.id = data
                    targ.data_path = f'["{side}"]'
                    
                    var = driv.variables.new()
                    var.name = 'FS'
                    var.type = 'SINGLE_PROP'
                    targ = var.targets[0]
                    targ.id_type = 'MESH'
                    targ.id = data
                    targ.data_path = '["aaa_fs"]'
                    
                    add = ''
                    if winners := suppressed.get(control):
                        add += applyDominationRules(driv, winners, add, sfx=sfx)
                    #add += '*FS'
                    
                    if N == 0:
                        #driv.expression = f'min(max(MLT*-1, 0), 1)*V1'+add
                        driv.expression = f'min(max(min(max(MLT*-1, 0), 1)*V1{add}, 0), 1)*FS'
                    if N == 1:
                        #driv.expression = 'min(max(1-abs(MLT), 0), 1)*V1'+add
                        driv.expression = f'min(max(min(max(1-abs(MLT), 0), 1)*V1{add}, 0), 1)*FS'
                    if N == 2:
                        #driv.expression = 'min(max(MLT*1, 0), 1)*V1'+add
                        driv.expression = f'min(max(min(max(MLT*1, 0), 1)*V1{add}, 0), 1)*FS'
    else:
        if is_stereo:
            for sfx in ['L', 'R']:
                key = KB.get(slider+sfx)
                if key == None:
                    if (key := repair_flex(control)) == False:
                        print(f'Failed to complete a pair for {control}!')
                        continue
                
                if sfx == 'L':
                    key.vertex_group = 'blendleft'
                if sfx == 'R':
                    key.vertex_group = 'blendright'
                
                key.driver_remove('value')
                driver = key.driver_add('value')
                driv = driver.driver
                
                side = left_format if sfx == 'L' else right_format
                
                var = driv.variables.new()
                var.name = 'V1'
                var.type = 'SINGLE_PROP'
                targ = var.targets[0]
                targ.id_type = 'MESH'
                targ.id = data
                targ.data_path = f'["{side}"]'
                
                var = driv.variables.new()
                var.name = 'FS'
                var.type = 'SINGLE_PROP'
                targ = var.targets[0]
                targ.id_type = 'MESH'
                targ.id = data
                targ.data_path = '["aaa_fs"]'
                
                add = ''
                if winners := suppressed.get(slider):
                    print(slider, winners)
                    add += applyDominationRules(driv, winners, add, sfx=sfx)
                #add += '*FS'
                #driv.expression = 'V1'+add
                driv.expression = f'min(max(V1{add}, 0), 1)*FS'
        else:
            key = KB.get(slider)
            if key == None: continue
            key.driver_remove('value')
            driver = key.driver_add('value')
            driv = driver.driver
            
            var = driv.variables.new()
            var.name = 'V1'
            var.type = 'SINGLE_PROP'
            targ = var.targets[0]
            targ.id_type = 'MESH'
            targ.id = data
            targ.data_path = f'["{slider_format}"]'
            
            var = driv.variables.new()
            var.name = 'FS'
            var.type = 'SINGLE_PROP'
            targ = var.targets[0]
            targ.id_type = 'MESH'
            targ.id = data
            targ.data_path = '["aaa_fs"]'
            
            add = ''
            if winners := suppressed.get(slider):
                add += applyDominationRules(driv, winners, add)
            #add += '*FS'
            #driv.expression = 'V1'+add
            driv.expression = f'min(max(V1{add}, 0), 1)*FS'
            
if final_do_wrinkles and do_wrinkles and bool(left_group) and bool(right_group):
    from functools import reduce
    mesh = data
    basis = KB[0]
    
    bL = left = left_group.index
    bR = right = right_group.index
    
    vertex = len(mesh.vertices)
    v_array = np.zeros(vertices*3, np.float32)
    left_mask = np.array([next(iter(filter(lambda a: a.group == left, vertex.groups)), null).weight for vertex in data.vertices])
    right_mask = np.array([next(iter(filter(lambda a: a.group == right, vertex.groups)), null).weight for vertex in data.vertices])
    
    basis.data.foreach_get('co', v_array)
    
    for name, attr_name, bak, mult in shapes:
        if (key := KB.get(name)) == None: continue
        movement = np.zeros(vertices*3, np.float32)
        
        key.data.foreach_get('co', movement)
        offset = np.reshape(movement - v_array, (vertices, 3))
        distances = np.linalg.norm(offset, axis=1)
        
        longest = reduce(lambda a, b: a if a > b else b, distances)
        
        distances /= longest
        
        if name.endswith('L'):
            distances *= left_mask
        if name.endswith('R'):
            distances *= right_mask
        
        if new_attr := data.attributes.get(attr_name):
            pass
        else:
            new_attr = data.attributes.new(attr_name, 'FLOAT', 'POINT')
        
        new_attr.data.foreach_set('value', distances)
    
    if (mod := obj.modifiers.get('HWM Wrinkles')) == None:
        mod = obj.modifiers.new('HWM Wrinkles', 'NODES')
        ng = bpy.data.node_groups.new('HWM Wrinkles', 'GeometryNodeTree')
        mod.node_group = ng
        NT = ng
        ng.interface.new_socket(name='Output', in_out='OUTPUT', socket_type='NodeSocketGeometry')
        ng.interface.new_socket(name='Input', in_out='INPUT', socket_type='NodeSocketGeometry')
    else:
        NT = mod.node_group
        ng = NT
    
    NT.animation_data_clear()
    for node in NT.nodes:
        NT.nodes.remove(node)

    input_node = ng.nodes.new('NodeGroupInput')
    store = ng.nodes.new('GeometryNodeStoreNamedAttribute')
    store.data_type = 'FLOAT2'
    store.domain = 'POINT'
    store.inputs[2].default_value = 'tension'
    
    output = ng.nodes.new('NodeGroupOutput')
    output_node = output
    
    combine = ng.nodes.new('ShaderNodeCombineXYZ')
    
    ng.links.new(combine.outputs[0], store.inputs[3])
    ng.links.new(input_node.outputs[0], store.inputs[0])
    ng.links.new(store.outputs[0], output_node.inputs[0])
    
    compress = filter(lambda a: a[1].endswith('C'), shapes)
    stretch = filter(lambda a: a[1].endswith('S'), shapes)
    
    compress_nodes = list()
    stretch_nodes = list()
    
    for n, items in enumerate(compress):
        name, attr_name, bak, mult = items
        state = name[-1]
        loc = [0, 0]
    
        ATTR = NT.nodes.new('GeometryNodeInputNamedAttribute')
        ATTR.inputs[0].default_value = attr_name
        ATTR.location = loc
        ATTR.name = 'ATTRIBUTE'
        OUT = ATTR.outputs[0]
        
        MULT = NT.nodes.new('ShaderNodeMath')
        MULT.operation = 'MULTIPLY'
        MULT.location = loc
        MULT.name = 'DRIVEN'
        driver = MULT.inputs[1].driver_add('default_value')
        var = driver.driver.variables.new()
        targ = var.targets[0]
        targ.id_type = 'KEY'
        targ.id = SK
        targ.data_path = f'key_blocks["{name}"].value'
        driver.driver.type = 'AVERAGE'
        
        MATH = NT.nodes.new('ShaderNodeMath')
        MATH.operation = 'MULTIPLY'
        MATH.location = loc
        MATH.name = 'SCALE'
        MATH.inputs[1].default_value = abs(mult)
        
        GAMMA = NT.nodes.new('ShaderNodeMath')
        GAMMA.operation = 'POWER'
        GAMMA.location = loc
        GAMMA.name = 'POWER'
        NT.links.new(ATTR.outputs[0], GAMMA.inputs[0])
        GAMMA.inputs[1].default_value = 0.4
        OUT = GAMMA.outputs[0]
        
        NT.links.new(OUT, MULT.inputs[0])
        NT.links.new(MULT.outputs[0], MATH.inputs[0])
        
        if n == 0:
            last = MATH.outputs[0]
        if n > 0:
            MAX = NT.nodes.new('ShaderNodeMath')
            MAX.name = 'MAXIMUM'
            MAX.operation = 'MAXIMUM'
            MAX.location = loc
            NT.links.new(last, MAX.inputs[0])
            NT.links.new(MATH.outputs[0], MAX.inputs[1])
            NT.links.new(MAX.outputs[0], combine.inputs[0])
            compress_nodes.append(MAX)
            last = MAX.outputs[0]
            
    for n, items in enumerate(stretch):
        name, attr_name, bak, mult = items
        state = name[-1]
        loc = [1000, 0]
    
        ATTR = NT.nodes.new('GeometryNodeInputNamedAttribute')
        ATTR.inputs[0].default_value = attr_name
        ATTR.location = loc
        ATTR.name = 'ATTRIBUTE'
        OUT = ATTR.outputs[0]
        
        MULT = NT.nodes.new('ShaderNodeMath')
        MULT.operation = 'MULTIPLY'
        MULT.location = loc
        MULT.name = 'DRIVEN'
        driver = MULT.inputs[1].driver_add('default_value')
        var = driver.driver.variables.new()
        targ = var.targets[0]
        targ.id_type = 'KEY'
        targ.id = SK
        targ.data_path = f'key_blocks["{name}"].value'
        driver.driver.type = 'AVERAGE'
        
        MATH = NT.nodes.new('ShaderNodeMath')
        MATH.operation = 'MULTIPLY'
        MATH.location = loc
        MATH.name = 'SCALE'
        MATH.inputs[1].default_value = mult
        
        GAMMA = NT.nodes.new('ShaderNodeMath')
        GAMMA.operation = 'POWER'
        GAMMA.location = loc
        GAMMA.name = 'POWER'
        NT.links.new(ATTR.outputs[0], GAMMA.inputs[0])
        GAMMA.inputs[1].default_value = 0.4
        OUT = GAMMA.outputs[0]
        
        NT.links.new(OUT, MULT.inputs[0])
        NT.links.new(MULT.outputs[0], MATH.inputs[0])
        
        if n == 0:
            last = MATH.outputs[0]
        if n > 0:
            MAX = NT.nodes.new('ShaderNodeMath')
            MAX.name = 'MAXIMUM'
            MAX.operation = 'MAXIMUM'
            MAX.location = loc
            NT.links.new(last, MAX.inputs[0])
            NT.links.new(MATH.outputs[0], MAX.inputs[1])
            NT.links.new(MAX.outputs[0], combine.inputs[1])
            compress_nodes.append(MAX)
            last = MAX.outputs[0]
    