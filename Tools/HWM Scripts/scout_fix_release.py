import bpy
from collections import defaultdict
import json
from string import ascii_lowercase as letters

C = bpy.context
obj = C.object
data = obj.data

true = True
false = False

group_controls = defaultdict(list)
eyelids = dict()
stereos = dict()
dominations = dict()
ranges = dict()

stereo_set = set()

slider_list = list()
flex_set = set()

for attr in filter(lambda a: getattr(a, 'name', '').startswith('SK.'), data.attributes):
    if '_' in attr.name: continue
    flex_set.add(attr.name[3:])
    
is_multi = dict()

def GroupControls(name, *argv):
    for arg in argv:
        group_controls[name].append(arg)
        flex_set.add(arg)
    if len(argv) == 2:
        ranges[name] = (-1, 1)
    if len(argv) != 2:
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
    for i in group_controls[name]:
        stereo_set.add(i)
        
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
 
 
-- reorder controls
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
    "TongueWidth"
);
 
 
SetEyelidControl("CloseLid", true );
 
-- setup stereo controls
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
SetStereoControl("TongueV", false );
SetStereoControl("TongueH", false );
SetStereoControl("TongueCurl", false );
SetStereoControl("TongueD", false );
 
 
-- add control dominators
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
'''.replace('--', '#')
''' END OF LUA PARAMETERS '''

exec(funcs)

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

if flex_map := data.get('flex_controllers', {}):
    flex_map = flex_map.to_dict()
else:
    for key, value in data.items():
        if not isinstance(value, float): continue
        split = key.split('_', maxsplit=1)
        if len(split) < 2: continue
        num, name = split
        try:
            int(''.join(map(lambda x: str(letters.find(x)), num)))
        except ValueError: continue
        
        flex_map[name] = key
        
for key in KB:
    if not '_' in getattr(key, 'name', ''): continue
    key.driver_remove('value')
    driver = key.driver_add('value')
    driv = driver.driver
    if key.name.endswith('R'):
        side = 'R'
        split = key.name[:-1].split('_')
        split = list(map(lambda a: (KB.get(a) or KB.get(a+side)), split))
        if None in split: continue
    elif key.name.endswith('L'):
        side = 'L'
        split = key.name[:-1].split('_')
        split = list(map(lambda a: (KB.get(a) or KB.get(a+side)), split))
        if None in split: continue
    else:
        split = key.name.split('_')
        split = list(map(lambda a: KB.get(a), split))
        if None in split: continue
    
    driver = key.driver_add('value')
    driv = driver.driver
    
    expr = ''
    
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
                    if key == None: continue
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
                    if key == None: continue
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
                    if key == None: continue
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
                if key == None: continue
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
            driv.expression = f'min(max(V1{add}, 0), 1)*FS'
            
if mod := obj.modifiers.get('wrinkle'):
    ng = mod.node_group
    if not ng.library:
        for driver in [driver.driver for driver in getattr(ng.animation_data, 'drivers', [])]:
            var = driver.variables[0]
            targ = var.targets[0]
            if targ.id_type == 'KEY': continue
            id = targ.id
            targ.data_path = targ.data_path[targ.data_path.find('.')+1:]
            targ.id_type = 'KEY'
            targ.id = id.shape_keys
for obj in bpy.data.objects:
    if isinstance(obj.get('script'), bpy.types.Text):
        del obj['script']