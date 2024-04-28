# Source Engine Blender Collection
The Source Engine Blender Collection is an asset library of models, materials and maps from Valve's Source games ported to Blender with efficiency and optimization in mind. Third party games are planned.

If you're wondering how optimizations are done, it's not as simple as drag and drop. That'd just be lazy. I first create a set of asset libraries made for the maps to link from, so they don't have duplicate assets. These asset libraries also serve as *actual* asset libraries for Blender, instead of just for the maps, allowing users to drag and drop assets from the game.

Models and maps are both ported with SourceIO and Plumber, to get the best out of both worlds. In the models' case, SourceIO is used for porting .mdl files and for its BVLG shader. Plumber is used for animations. In the maps' case, SourceIO is used for its ropes, and Plumber is used to port the actual map.

Once the maps are ported, they go through a process of going through every mesh and material to see if they already exist in the pre-existing libraries. If they do, then use the existing asset. If they don't, then do nothing. This allows for a massive downsizing operation that is just incomparable to importing maps without any optimizations. .EXR files from maps are converted to DWAA format to save as much space as possible with little compromise to quality.

## Map Extras
### Fog
Tons of Source games use a fog effect in their gameplay, and fortunately that shader is easy to recreate. To mess around with the fog settings in a map, head over to the `Tools` tab and open up the `Fog Properties`. From there, you can adjust the fog strength, minimum and maximum distances, and the color gradient the fog uses.  
![image](https://github.com/hisprofile/blenderstuff/assets/41131633/117340c8-c37e-46df-b883-128486f05f35)

### Overlays Offset
Overlays in the map usually have clipping issues, which can make a render look really ugly upon a render. In the `Map Extras` tab lies a panel named `Overlays Offset`. You can randomize the offset in case of overlays overlapping each other. `Decal Collection` can be set for a custom set of meshes to fix. If left empty, it will fix all overlays in the `overlays` collection by default. When ready, click `Offset Overlays`. All overlays will be offset by their normal scaled by the inputted sizes.

![image](https://github.com/hisprofile/blenderstuff/assets/41131633/7fc3d3c5-9179-4301-9b11-2efe47ce1473)

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

## Tips
### Fixing Skybox  
Look for an empty object labelled "sky_camera." Around this empty should be lots of little pieces of meshes. Select the `sky_camera` object first, then box select (B) the surrounding objects. However, if you see the enitre map mesh is highlighted, then you need to enter `Edit Mode` on the world mesh labelled "worldspawn". Select the mesh surrounding the empty with the box select tool then separate it (P, Separate selection). Enter `Object Mode`, select the `sky_camera`, box select the surrounding mesh, then go to the `Object tab > Transform VMF 3D Sky`. If the entire map moves with the `sky_camera` object, that means you did not separate all of the mesh around the empty, or you accidentally had it selected while transforming the 3D sky.

### Injecting Data
`_resources.blend` contains two major node groups named `Resources-ShaderN Container` and `Resources-GeoN Container`. These two node groups contain every node group used by the materials, models, and maps. These node groups can have more node groups added under them. That way, any new node group will be available in any .blend file you open. This makes for extremely easy editing across .blend files, minimizing the amount that would alternatively be needed.

### Opening asset .blend files  
In the ported map files, you can open the .blend file of any linked prop or material. You can find this under the `Linked Properties` panel of any mesh or material tab. Clicking the operator will open the .blend file, and shift + clicking will reload the .blend file to apply the change. Make sure you save the file first!

## Installation Instructions  
To install an archive of the Source Engine Blender Collection, you must first allocate a folder for a game collection. Then, download `_resources.blend` and `blender_assets.cats.txt`. `_resources.blend` is required regardless of what you decide to download. It serves as a resource pack for the models and materials to reuse data from. `blender_assets.cats.txt` is required for Blender's asset library functionality, allowing you to add the allocated folder as an asset library.

To download the actual content, download the `_materials` and `_models` folders. Download the `_actions` folder if you wish for animations. I don't recommend downloading the entirety of the maps at once, so just make a folder named `_maps` and download the maps you need or want when you need or want them.

To add the archive as an asset library for Blender, head to `Edit > Preferences > File Paths > Asset Libraries` and add the archive folder.

# [Counter Strike: Source](https://drive.google.com/drive/folders/1of8KW9hoPiAwLG7pJjXT6tauQFlWrL9S?usp=sharing)
Download ^

# [Counter Strike: Global Offensive](https://drive.google.com/drive/folders/1CTBdu8VhvBP767WJZb9_d4xO8EjBP51F?usp=sharing)
A ported archive of most CS:GO's models, materials, and maps. Resulting in a **massive** 20GB download. If you download this, I salute you.

I'll give an exact count of the number of models and materials that exist, but for the time being, I'm sure it's well over 10000 models. 

# [Portal 2](https://drive.google.com/drive/folders/1lzXtGsDhARhL_Y90Bn_HngGfjXk5Ngpo)
## Tips
### 4Panels
It seems that panel arms (I don't know what they're called) don't move the panel they are attached to automatically. It seems the solution is to close it using its close action, select the panel, then parent it to one of the moving bones. `props_ingame/arm_4panel/@ramp_90_deg_close` seems to work.  

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/d7381a85-3479-4a28-8377-794067c04bb8" width=40%>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/e316b170-01d4-498c-9647-200096bb6380" width=40%>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/aeaa8f3e-5c67-4164-81cb-d643e291f499" width=40%>

## Effects
### Hard Light Bridge
Prop `props/wall_emitter` has a geometry nodes effect linked as a custom property. To use it, add a geometry nodes group and set the node group to `Hard Light Bridge`  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/0510ea5d-c192-4a04-9890-d6086b1d4094">

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

##### [Plumber by lasa01](https://github.com/lasa01/Plumber/releases), [SourceIO by REDxEYE](https://github.com/REDxEYE/SourceIO/releases)
