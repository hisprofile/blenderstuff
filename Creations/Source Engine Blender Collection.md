# Source Engine Blender Collection
The Source Engine Blender Collection is an asset library of models, materials and maps from Valve's Source games ported to Blender with efficiency and optimization in mind. Third party games are planned.

If you're wondering how optimizations are done, it's not as simple as drag and drop. That'd just be lazy. I first create a set of asset libraries made for the maps to link from, so they don't have duplicate assets. These asset libraries also serve as *actual* asset libraries for Blender, instead of just for the maps, allowing users to drag and drop assets from the game.

Models and maps are both ported with SourceIO and Plumber, to get the best out of both worlds. In the models' case, SourceIO is used for porting .mdl files and for its BVLG shader. Plumber is used for animations. In the maps' case, SourceIO is used for its ropes, and Plumber is used to port the actual map.

Once the maps are ported, they go through a process of going through every mesh and material to see if they already exist in the pre-existing libraries. If they do, then use the existing asset. If they don't, then do nothing. This allows for a massive downsizing operation that is just incomparable to importing maps without any optimizations. .EXR files from maps are converted to DWAA format to save as much space as possible with little compromise to quality.

## Tips
### Fog
Tons of Source games use a fog effect in their gameplay, and fortunately that shader is easy to recreate. To mess around with the fog settings in a map, head over to the `Tools` tab and open up the `Fog Properties`. From there, you can adjust the fog strength, minimum and maximum distances, and the color gradient the fog uses.  
![image](https://github.com/hisprofile/blenderstuff/assets/41131633/117340c8-c37e-46df-b883-128486f05f35)

### Fixing Skybox  
Look for an empty object labelled "sky_camera." Around this empty should be lots of little pieces of meshes. Select the `sky_camera` object first, then box select (B) the surrounding objects. However, if you see the enitre map mesh is highlighted, then you need to enter `Edit Mode` on the world mesh labelled "worldspawn". Select the mesh surrounding the empty with the box select tool then separate it (P, Separate selection). Enter `Object Mode`, select the `sky_camera`, box select the surrounding mesh, then go to the `Object tab > Transform VMF 3D Sky`. If the entire map moves with the `sky_camera` object, that means you did not separate all of the mesh around the empty, or you accidentally had it selected while transforming the 3D sky.

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
