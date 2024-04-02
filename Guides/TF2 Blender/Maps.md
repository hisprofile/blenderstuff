# [Maps](https://drive.google.com/drive/u/1/folders/1J2-Ahbw1xbJodzqRVX4cXbg6EKHhe7we)  

The TF2 Map Pack is a collection of every Team Fortress 2 map ported to Blender, in the _highest_ quality possible. The whole thing is chock-full of features to make using the map pack an obvious choice over porting them yourself.
[Download link](https://drive.google.com/drive/u/1/folders/1J2-Ahbw1xbJodzqRVX4cXbg6EKHhe7we)

# The Features  
## Proximity Lights  

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/01cdc3fd-0c16-4599-b417-0f6425633a56" width=30%>  

This feature is more useful to EEVEE.

EEVEE's light limit is hardcapped at 127 due to technical limitations. This is a problem, as most of the maps exceed that light limit. The solution to this is an addon that disables lights when too far from the active camera, a distance threshold determined by the user. This is updated every frame.  
[Proximity Lights documentation](https://github.com/hisprofile/ProximityLights/blob/main/README.md)

### Optimizing lights: Method 1
Use the addon as instructed

### Method 2
Use geometry nodes. will add more info later

## Prop(er) Skins  
A lot of props have different ["skins"](https://developer.valvesoftware.com/wiki/Skin), so you can use lots of different materials on the same prop. When you import a material through [SourceIO](https://github.com/REDxEYE/SourceIO) or [Plumber](https://github.com/lasa01/Plumber), these props will **always** have their default skin, which isn't good if you're looking for 1:1 representation.

In the TF2 Map Pack, EVERY prop has their correct skin as mentioned in the map files.[^1]

Reference  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/fd56dc95-c2ac-4c6f-aec7-237f0c5d7d48" width=50%>

TF2 Map Pack  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/c25b42f9-6195-4afe-99ac-1f53d83a0aba" width=50%>  
[Cycles Render 2](https://github.com/hisprofile/blenderstuff/assets/41131633/9ce6e0e3-c439-49fa-af4f-e0b10dc56bf6)  
[EEVEE Legacy Render](https://github.com/hisprofile/blenderstuff/assets/41131633/7a4cbf30-921d-4adc-9e74-a77cdcd67d4d)  

[SourceIO](https://github.com/REDxEYE/SourceIO)  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/d1b7d31d-9404-49ae-a529-55c5444146a4" width=50%>

[Plumber](https://github.com/lasa01/Plumber)  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/c42a1a0a-b7b5-428a-969a-9ce380186bc9" width=50%>

## Texture Scrolling
Objects like waterfalls or materials like lava support texture scrolling, making them less static. The speed at which they scroll is constant across framerates. You can adjust the speed at which they scroll in the modifier panel.

## A LOT of Space Saved.  
Yes, it's true. You *could* port the maps yourself given the right tools and addon. However, no addon out there uses space-saving techniques that the map pack uses. 
- All textures are saved in PNG
  - The alternative is .tga, which cannot be easily compressed. Because .png has lossless compression, it's a no brainer which texture format should be used.[^2]
- Models, materials, and textures are re-used.
  - There are two archives every map relies on: _props.blend and _materials.blend
    - _props.blend contains every prop in TF2's game files, along the materials and textures the props use.
    - _materials.blend contains every material and texture in TF2's game files, mostly the materials used by maps

Without optimizations, the map pack would stand at 170+gb. With all the optimizations? Less than 7gb. That's just astounding!  
[TF2 Map Pack spec sheet](https://drive.google.com/file/d/1WwQ4-EDfTMbCfevu-W5o_vTkZIl8iEFS/view)

# The Disadvantages
General roadblocks and issues you may run into.
## Difficult to edit
Because most of the assets (models, materials) in each map are linked/reused from other .blend files, the only way to alter an asset is to localize it by clicking on the <img src="https://github.com/Shrinks99/blender-icons/blob/main/blender-icons/linked.svg" height=20> chain icon next to an asset's name. This is because you cannot directly edit assets/data blocks used from another .blend file. Localizing a data block creates a copy for the .blend file you're working in.

If there is no chain next a data block's name, then the data block is localized.

### Editing a Mesh  
Navigate to the <img src="https://raw.githubusercontent.com/Shrinks99/blender-icons/e00f65a942cdd66206bdb454e33798b4199a6ae3/blender-icons/outliner_data_mesh.svg" height=20> mesh data tab of the active object, find the mesh name and click on the <img src="https://github.com/Shrinks99/blender-icons/blob/main/blender-icons/linked.svg" height=20> chain icon. You should now be able to edit the mesh of an object.

### Editing a Material
First, localize the mesh that is using the material in question, then navigate to the <img src="https://raw.githubusercontent.com/Shrinks99/blender-icons/e00f65a942cdd66206bdb454e33798b4199a6ae3/blender-icons/material_data.svg" height=20> material tab and localize the material.

### Editing a Texture
First, localize the mesh and material of the object in question. Navigate to the shader node editor of the material who's texture you want to edit. Find the node of said texture and click on the chain icon to localize.

### Editing a node group
First, localize the mesh and material of the object in question. Navigate to the shader node editor of the material who's node group you want to edit. Find the node group and click on the chain icon to localize.

## Lighting isn't the same  
This mostly applies to EEVEE Legacy, as it has no native support for real-time global illumination. In general, the ambience of the map will never be 1:1 between Blender and TF2 no matter what render engine you use. Despite that, Cycles will always appear closer.

When baking a map, the HAMMER editor performs an effect like [global illumination](https://en.wikipedia.org/wiki/Global_illumination) onto areas of the map to give the ambience a semi-realistic feel. It will then save that data to use in-game. For example, a light will light up most parts of the room because the light bounces everywhere. This data is not recoverable when porting a map. Therefore, using a map in EEVEE Legacy can make the ambience feel lackluster. There are two remedies for this solution:

### Using [Irradiance Volumes](https://docs.blender.org/manual/en/latest/render/eevee/light_probes/irradiance_volumes.html)  
Irradiance volumes will bake the ambience of its surroundings to then project off of its surroundings. This can be considered global illumination, but it is not real-time.

### Altering World Shader  
Depending where the camera is in a map, you can brighten or darken the world shader through the `TF2 Ambience` node through the `Color` and `Strength` values to whatever feels right at the time. These values can be keyframed.

## Performance Issues
Because Blender isn't as realtime as the Source engine, adding more objects in a scene tends to slow down performance. It helps to delete parts of the map you won't use in your render. You can delete props and lights in object mode, then parts of the map in edit mode.

## Prop Animations
Props that have animations in-game *should* have their animations in the ports. These animations are FPS locked, so if you wish to repeat them or change the speed, I recommend pushing down actions to the NLA editor and editing them there.

# The Improvements
Improvements you can make to the map.

## Water Animation
Texture animations cannot be packed into a .blend file, so they need to be external. To use water animations:
1. Download the `water_animation` folder from the drive and place it next to `_materials.blend` (in the same folder.)
2. Enter edit mode on the world mesh, use `Face Select` mode, and select the face of a water mesh. This is to switch to the material of the face in the shader editor, which should be a water shader.
3. [Localize](https://github.com/hisprofile/blenderstuff/blob/main/Guides/TF2%20Blender/Maps.md#editing-a-material) the material.
4. In the water shader, there *should* be a separate animated texture node. Swap out the default water texture node with the animated one.

## Adding Fog
In the <img src="https://raw.githubusercontent.com/Shrinks99/blender-icons/e00f65a942cdd66206bdb454e33798b4199a6ae3/blender-icons/scene_data.svg" height=20> scene properties, there *should* be a panel named `TF2 Map Pack Properties` with a box labeled `Fog Properties.` There, you can edit the strength of the fog, the start and end, and the starting and ending color of the fog. If some parts of the map do not have the fog effect applied to them, using the `Finalize Fog` tool should apply it on every material that doesn't yet have it.

This is a real-time solution. An alternative method is to use the compositor and mixing the render result with a solid color using the depth or mist pass as a factor.

# The Installation
If I may be informal: If you somehow mess up the installation, I'd be surprised since it's so simple. Though If it's my fault, I sincerely apologize.

All maps **require** `_materials.blend` and `_props.blend` to be in the same folder as the maps, as they are asset libraries for the map ports. Like what `.vpk` files are for TF2. Create a folder for the TF2 Map Pack, and place `_materials.blend` and `_props.blend` into that folder. Then, place whatever map you'd like to use into that folder. That's it.

If you'd like to move the maps somewhere else, you can create a duplicate using `Save As`, and saving it into another folder. This should keep the connection with the assets. If you don't want a duplicate, just delete the original file.

# The Extras
- All payload maps have paths created for the carts. You can change how far along the cart is on the path in the <img src="https://raw.githubusercontent.com/Shrinks99/blender-icons/e00f65a942cdd66206bdb454e33798b4199a6ae3/blender-icons/constraint.svg" height=20> constraints tab.
- A folder named `exr_skybox` in the TF2 Map Pack containts an .exr version of all the skyboxes used by the maps.
- You can view the `Map Pack Spec Sheet` in the drive to see the statistics of all the maps. This includes file sizes (after, before, difference), object count and light count. The total space saved is at the bottom of the `.txt` file.
- In EEVEE, you can add reflection planes onto the water for off-screen reflections.

[^1]: Props not included in TF2's `.vpk` files will not have their correct skins.
[^2]: At the time of porting, Plumber only offered textures to be saved as .tga files. A rigorous process was used to convert these .tga files to .png for smaller file sizes.
