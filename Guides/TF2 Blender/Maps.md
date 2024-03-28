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
A lot of props have different "skins", so you can use lots of different materials on the same prop. When you import a material through [SourceIO](https://github.com/REDxEYE/SourceIO) or [Plumber](https://github.com/lasa01/Plumber), these props will **always** have their default skin, which isn't good if you're looking for 1:1 representation.

In the TF2 Map Pack, EVERY prop has their correct skin as mentioned in the map files.[^1]

## Texture Scrolling
Objects like waterfalls or materials like lava support texture scrolling, making them less static. The speed at which they scroll is constant across framerates. You can adjust the speed at which they scroll in the modifier panel.

## A LOT of Space Saved.  
Yes, it's true. You *could* port the maps yourself given the right tools and addon. However, no addon out there uses space-saving techniques that the map pack uses. 
- All textures are saved in PNG
  - The alternative is .tga, which cannot be easily compressed. Because .png has lossless compression, it's a no brainer which texture format should be used.
- Models, materials, and textures are re-used.
  - There are two archives every map relies on: _props.blend and _materials.blend
    - _props.blend contains every prop in TF2's game files, along the materials and textures the props use.
    - _materials.blend contains every material and texture in TF2's game files, mostly the materials used by maps

Without optimizations, the map pack would stand at 170+gb. With all the optimizations? Less than 7gb. That's just astounding!  
[TF2 Map Pack spec sheet](https://drive.google.com/file/d/1WwQ4-EDfTMbCfevu-W5o_vTkZIl8iEFS/view)

# The Disadvantages
## 
