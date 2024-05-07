# Source Engine Blender Collection
Welcome to the **Source Engine Blender Collection!** A Blender archive of **45,000+** models, **45,000+** materials, and **550+** maps ported from eight of Valve's Source games! These ports were made with optimization and efficiency in mind, while catering to ease of usability. Below, you will find the installation instructions, download links for the eight archives, and general tips you may find useful. I've jam-packed this with features and nifty tricks, so this is definitely worth a read!

## What's included?
Each model 

The Source Engine Blender Collection is an asset library of models, materials and maps from Valve's Source games ported to Blender with efficiency and optimization in mind. Third party games are planned.

The Source Engine Blender Collection is a collection of archives of ports from eight of Valve's Source engine games, retaining the highest quality possible. These archives can be used as asset libraries to drag and drop models or materials from. 

If you're wondering how optimizations are done, it's not as simple as drag and drop. That'd just be lazy. I first create a set of asset libraries made for the maps to link from, so they don't have duplicate assets. These asset libraries also serve as *actual* asset libraries for Blender, instead of just for the maps, allowing users to drag and drop assets from the game.

Models and maps are both ported with SourceIO and Plumber, to get the best out of both worlds. In the models' case, SourceIO is used for porting .mdl files and for its BVLG shader. Plumber is used for animations. In the maps' case, SourceIO is used for its ropes, and Plumber is used to port the actual map.

Once the maps are ported, they go through a process of going through every mesh and material to see if they already exist in the pre-existing libraries. If they do, then use the existing asset. If they don't, then do nothing. This allows for a massive downsizing operation that is just incomparable to importing maps without any optimizations. .EXR files from maps are converted to DWAA format to save as much space as possible with little compromise to quality.

## Map Extras
### Fog
Tons of Source games use a fog effect in their gameplay, and fortunately that shader is easy to recreate. To mess around with the fog settings in a map, head over to the `Tools` tab and open up the `Fog Properties`. From there, you can adjust the fog strength, minimum and maximum distances, and the color gradient the fog uses.  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/4897ea4a-f2e6-4bd5-842a-5b8724320e25" width=70%>

### Overlays Offset
Overlays in the map usually have clipping issues, which can make a render look really ugly upon a render. In the `Map Extras` tab lies a panel named `Overlays Offset`. You can randomize the offset in case of overlays overlapping each other, or in case the overlays are clipping into a map. `Decal Collection` can be set for a custom set of meshes to fix. If left empty, it will fix all overlays in the `overlays` collection by default. When ready, click `Offset Overlays`. All overlays will be offset by their normal scaled by the inputted sizes.

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/1c059439-1d0c-4c8d-b62f-be58c49ac3bd" width=70%>


### Delete Materials from Faces
Tons of unneeded materials such as `toolsnodraw` and `toolsblack` can pollute a file with unneeded geometry. Despite not being visible in EEVEE, they can produce visual errors in Cycles through Z-fighting. Deleting this geometry through a node group is a fast solution, and is applied to every object of a collection by batch. Set the material you wish to be deleted and click `Delete Material`. `Remove "Delete Material" Node Group` will delete every node group targeted the selected material. Shift clicking this operator will delete every node group regardless of material.

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/990eb4a4-e66c-4344-a269-dbd43d9a0c9d" width=70%>

### Proximity Lights  

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/01cdc3fd-0c16-4599-b417-0f6425633a56" width=30%>  

This feature is more useful to EEVEE.

EEVEE's light limit is hardcapped at 127 due to technical limitations. This is a problem, as most of the maps exceed that light limit. The solution to this is an addon that disables lights when too far from the active camera, a distance threshold determined by the user. This is updated every frame.  
[Proximity Lights documentation](https://github.com/hisprofile/ProximityLights/blob/main/README.md)

#### Optimizing lights: Method 1 (Slower, more flexible)
Use the addon as instructed

#### Method 2 (Faster, less flexible)
Use geometry nodes.
[Proximity Lights - Geometry Nodes Version](https://github.com/hisprofile/blenderstuff/blob/main/Tools/Proximity%20Lights%20-%20Geometry%20Nodes/Documentation.md)

### Extensions
Every good project should have a way for users to mod it, and so I introduce extension loader! A non-destructive way for users to add their own scripts. Upon loading a map, the .blend file will check if a folder named `_extensions` exists in the archive root directory. If it does, it will go through all .py files under the folder and load them. It should be structured like a regular Blender addon, sans any code executing a register function.

Example:
<details>
  <summary>Extension example</summary>

  ```py
import bpy

from bpy.types import Operator, Panel

class MAPPACK_subpanel(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Tool'
    bl_parent_id = 'MAPPACK_PT_panel'
    bl_options = {'DEFAULT_CLOSED'}
    
class MAPPACK_OT_open_drive(Operator):
    bl_idname = 'port.open_drive_link'
    bl_label = 'Open Google Drive Folder'
    bl_description = 'Open the link to the Google Drive folder for this archive'
    
    def execute(self, context):
        bpy.ops.wm.url_open(url='https://drive.google.com/open?id=10IZLq5VTM1S2B3D4UBdXLMO0tuZC8jq7&usp=drive_fs')
        return {'FINISHED'}

class MAPPACK_PT_drive_panel(MAPPACK_subpanel):
    bl_label = 'Drive Folder'
    
    def draw(self, context):
        layout = self.layout
        layout.operator('port.open_drive_link')

classes = [
    MAPPACK_OT_open_drive,
    MAPPACK_PT_drive_panel
]
    
def register(a=None, b=None):
    for i in classes:
        bpy.utils.register_class(i)

def unregister(a=None, b=None):
    for i in reversed(classes):
        bpy.utils.unregister_class(i)
```
  
</details>

## Tips
### Fixing Skybox  
Look for an empty object labelled "sky_camera." Around this empty should be lots of little pieces of meshes. Select the `sky_camera` object first, then box select (B) the surrounding objects. However, if you see the enitre map mesh is highlighted, then you need to enter `Edit Mode` on the world mesh labelled "worldspawn". Select the mesh surrounding the empty with the box select tool then separate it (P, Separate selection). Enter `Object Mode`, select the `sky_camera`, box select the surrounding mesh, then go to the `Object tab > Transform VMF 3D Sky`. If the entire map moves with the `sky_camera` object, that means you did not separate all of the world mesh around the empty, or you accidentally had it selected while transforming the 3D sky.

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/28c8dcea-8a6c-436e-ba94-5b008f7f7a28" width=70%>

Here, I am separating the world mesh around the skybox by pressing P. Once separated, I select the `sky_camera` empty, then mesh surrounding, then I go to `Object > Transform VMF 3D Sky`

### Injecting Data
`_resources.blend` contains two major node groups named `Resources-ShaderN Container` and `Resources-GeoN Container`. These two node groups contain every node group used by the materials, models, and maps. These node groups can have more node groups added inside them. That way, any new node group will be available in any .blend file you open. This makes for extremely easy editing across .blend files, minimizing the amount that would alternatively be needed.

### Opening asset .blend files  
In the ported map files, you can open the .blend file of any linked prop or material. You can find this under the `Linked Properties` panel of any mesh or material tab. Clicking the operator will open the .blend file, and shift + clicking will reload the .blend file to apply the change. Make sure you save the file first!

## Installation Instructions  
To install an archive of the Source Engine Blender Collection, you must first allocate a folder for a game collection. Then, download `_resources.blend` and `blender_assets.cats.txt`. `_resources.blend` is required regardless of what you decide to download. It serves as a resource pack for the models and materials to reuse data from. `blender_assets.cats.txt` is required for Blender's asset library functionality, allowing you to add the allocated folder as an asset library.

To download the actual content, download the `_materials` and `_models` folders. Download the `_actions` folder if you wish for animations. I don't recommend downloading the entirety of the maps at once, so just make a folder named `_maps` and download the maps you need or want when you need or want them.

If you plan to download all of the files at once, chances are the .zip files will be split into multiple pieces. Extracting it is a matter of selecting all of the zip files and extracting them all. All of the files will be merged into a complete piece.
![image](https://github.com/hisprofile/blenderstuff/assets/41131633/31a7ad0c-71e8-49db-8e18-6123a34cf2f6)

A downloaded and extracted archive should look like this:
![image](https://github.com/hisprofile/blenderstuff/assets/41131633/7b4889dd-bece-46a5-88c0-5f1dd7a37014)

Depending on how you choose to download the archive, your installation may be different.

To add the archive as an asset library for Blender, head to `Edit > Preferences > File Paths > Asset Libraries` and add the archive folder.

# [Counter Strike: Global Offensive](https://drive.google.com/drive/folders/1CTBdu8VhvBP767WJZb9_d4xO8EjBP51F?usp=sharing)
A ported archive of CS:GO's assets, resulting in **23,504** models, **28,928** materials (19,078 usable out of asset library) and 89 maps. Totalling 18.2 GB. If you download all of this, I salute you.

# [Counter Strike: Source](https://drive.google.com/drive/folders/1of8KW9hoPiAwLG7pJjXT6tauQFlWrL9S?usp=sharing)
A ported archive of CS:S's assets, resulting in 3,519 models, 9,034 materials (6,817 usable out of asset library) and 20 maps. Totaling 2.66 GB/

# [Day of Defeat: Source](https://drive.google.com/open?id=1h-DnOF7lrogJayxH2rrqnO0VPs9MscU6&usp=drive_fs)
A ported archive of Day of Defeat: Source's assets, resulting in 691 models, 1,673 materials (602 usable out of asset library) and nine maps. Totalling 839.84 MB.

# [Half-Life: 2](https://drive.google.com/open?id=1OWx390SGmthg1sLOQwW_6X0YWyWVxnS7&usp=drive_fs)
A ported archive of Half-Life: 2's assets, resulting in 3,217 models, 6,791 materials (4968 usable out of asset library) and 118 maps. Totalling 2.09 GB. Half-Life 2: Episode One and Two are included.

# [Left 4 Dead 1/2](https://drive.google.com/open?id=1Xymp5cf11V5edquQu5tdwxxVPU3FxNEU&usp=drive_fs)
A ported archive of Left 4 Dead 2's assets, resulting in 5,497 models, 8,165 materials (4,999 usable out of asset library) and 60 maps. Totalling 4.45 GB.

Making L4D2's [infected](https://developer.valvesoftware.com/wiki/Infected_(shader)) was stupidly complicated. It uses at most three textures to generate over 20K unique zombies in specific cases. It tiles the R and G channel into a 2x2 square for different blood, specularity, dirt and retro-reflectivity masking. To use it properly, you'd have to use it as a sprite sheet. The R and G channel are centered at 127, and any value towards 0 or 255 has a different effect. Lower R channel masks specularity, upper R channel masks dirt, lower G channel masks retro-reflectivity and upper G channel masks blood. Think of breaking two sticks down the middle and holding them at their ends. You'd now have four unique sticks that may or may not have their own unique purpose. (I don't know, use your imagination)

To choose a color for a zombie, the B channel, the alpha channel, and a gradient map is used. The gradient map is 16 pixels tall and 256 pixels wide. The upper eight pixels are for skin tones and the lower eight are for clothing. If the B channel picks the rows of the column. is above 127, that means it will choose a random skin tone color from the upper eight rows. Else, choose a random clothing color from the lower eight rows. The alpha channel is used to choose the column of the gradient map.

It's oddly efficient and capable. 2009 game development was crazy!

## Credits
Syborg64 - Helped with infected shader
мяFunreal - [Infected Shader guide](https://steamcommunity.com/sharedfiles/filedetails/?id=1567031703&preview=true)

# [Portal](https://drive.google.com/open?id=15Pig2xn_8GHnraw3bsDN0o50dfnbb1qs&usp=drive_fs)
A ported archive of Portal's assets, resulting in 316 models, 504 materials (269 usable out of asset library) and 26 maps. Totalling 220.07 MB.

# [Portal 2](https://drive.google.com/drive/folders/1lzXtGsDhARhL_Y90Bn_HngGfjXk5Ngpo)
A ported archive of Portal 2's assets, resulting in 2,216 models, 3,629 materials (2,521 usable out of asset library) and 116 maps. Totalling 1.99 GB.

<details>
<summary>Tips</summary>

## Tips
### 4Panels
It seems that panel arms (I don't know what they're called) don't move the panel they are attached to automatically. It seems the solution is to close it using its close action, select the panel, then parent it to one of the moving bones. `props_ingame/arm_4panel/@ramp_90_deg_close` seems to work.  

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/d7381a85-3479-4a28-8377-794067c04bb8" width=40%>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/e316b170-01d4-498c-9647-200096bb6380" width=40%>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/aeaa8f3e-5c67-4164-81cb-d643e291f499" width=40%>
</details>

## Effects
### Hard Light Bridge
Prop `props/wall_emitter` has a geometry nodes effect linked as a custom property. To use it, add a geometry nodes group and set the node group to `Hard Light Bridge`  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/0510ea5d-c192-4a04-9890-d6086b1d4094">

## Credits
[Lil' Boneless Pizza](https://twitter.com/lilnobonepizza) - Helped with the Flowmap shader

# [Team Fortress 2](https://drive.google.com/drive/folders/10IZLq5VTM1S2B3D4UBdXLMO0tuZC8jq7)
A ported archive of Team Fortress 2's assets, resulting in 7,627 models, 16,602 materials (10,055 usable out of asset library) and 185 maps. Totalling 7.55 GB

# Source to Blender Porting Tools - hisanimations
[Porting Tools .zip](https://github.com/hisprofile/blenderstuff/raw/main/Creations/source_blender_porting_tools.zip)  
[Modified Addons](https://github.com/hisprofile/blenderstuff/blob/main/Creations/modified_addons.zip)

This is a set of porting tools to build an asset library of all models and materials of a source game for Blender. This asset library will then be used for the maps to reuse data, significantly lowering the size of the maps. When all is said and done, you should have a complete archive of the game you are trying to port.

All tools for the .blend files reside in the `TOOLS` tab in Blender. Any tweaking done should only have to be done in there.

To start, you must first create a folder for the game you wish to port from. This folder should contain all of the porting tools in the .zip file.

Prepare for all the assets you wish to port. Extract the models and materials from a game's `.vpk` archives and place them in the game folder. For example, to extract HL2's assets, you would extract any folder named `models` or `materials` and place them all under the `hl2` folder. For something like garry's mod, you should have something that looks like `garrysmod\models` and `garrysmod\materials`. This is where SourceIO and Plumber are going to look for assets. Gather all the `.bsp` files you want to port and decompile them with [bspsrc](https://github.com/ata4/bspsrc/releases) into `.vmf` files. They can be placed anywhere. In the `Other` tab of `bspsrc`, enable `Extract embedded files`. If you wish to add the embedded files as assets for the asset library, run the `move_vmf_files.py` script in the `slipup.blend` file of the porting tools. Set the `game` variable of the script to the game folder you are porting from, and set `root_dir` to the folder containing the `.vmf` files. Any detected model or material will be moved over to the game folder.

Once you have prepared all the assets you want to port, install hisanimations' versions of SourceIO and Plumber. If these addons already exist in your Blender's `addons` folder, rename them to keep a backup. Once you have installed the modified version of Plumber, make sure the game you want to port from is listed as a game directory.

Before you actually start porting any of the tools, I **HIGHLY** recommend that you keep the console open to view progress and check for any errors, such as whether textures or materials can be found or not.
## _models_porter.blend (Step 1)
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/960026fc-40be-44e6-8b89-fdbc0dcd27fe" height=300>  

Open `_models_porter.blend` and set the `models/ Folder` path to the `models` folder you want to port from. Set `Asset Folder Save Path` to where you want the models to be saved. `//` means it will be saved alongside `_models_porter.blend` (recommended). Hit `Create Catalogs` for creating the asset library, then click `Start Batch Job` to port the models. Two files and two folders will be created. `_mapper_models.json`, `_mapper_materials.json`, `_models` and `_actions`. The two .json files serve as directions for porting the maps. They are used to check if an asset already exists, and if it does, it will return the `.blend` file it is located in and what it is known as. Hopefully within an hour, the porting tool will have ported all of the models and saved them as `.blend` files.

## _materials_porter.blend (Step 2)
Open `_materials_porter.blend` and set the `materials/ Folder` path to the `materials` folder you want to port from. Set `Asset Folder Save Path` to where you want the models to be saved. `//` means it will be saved alongside `_materials_porter.blend` (recommended). Hit `Create Catalogs` for creating the asset library, then click `Start Batch Job` to port the materials. A folder named `_materials` will be created to store all of the materials. Eventually, the porting tool will have ported all of the materials and saved them as `.blend` files.

## _maps_porter.blend (Step 3)
Set `.VMF Maps Folder` to the folder containing all of the decompiled maps. Set `.BSP Maps Path` to the folder containing all of the `.bsp` versions of the maps. Set `Asset Folder Save Path` to where you want the models to be saved. `//` means it will be saved alongside `_maps_porter.blend`. Set `Game Folder` to the game folder. This folder should have the `models` and `materials` folder under it. Set `Games:` to the game you are attempting to port from. Once ready, hit `Start Batch Porting`.

# To-Do
- Fix decals to be fog compatible
- Port and rig SFM version of L4D2 survivors
- Port and rig Chell

# Credits
[Plumber](https://github.com/lasa01/Plumber/releases) - Maps, animations
[SourceIO](https://github.com/REDxEYE/SourceIO/releases) - Models, materials, ropes

##### [Plumber by lasa01](https://github.com/lasa01/Plumber/releases), [SourceIO by REDxEYE](https://github.com/REDxEYE/SourceIO/releases)
