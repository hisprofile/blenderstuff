# Rigs  
There are three official rig-sets usable by the TF2-Trifecta. They are referred to after the name of their creators.  

At their core, every single rig functions the same as they use Rigify for controls. The rigs were specially built to maintain the original bone orientations of their decompiled rigs, making cosmetic attachments possible. Other than that, you can learn how Rigify works by reading [Rigify's documentation](https://docs.blender.org/manual/en/latest/addons/rigging/rigify/index.html). What's worth mentioning is that you can alter the rig in the `Item` tab in Blender's viewport. Selecting different bones will show different properties through which you can manipulate the rig.

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/6bb8212c-df0c-47d0-af3f-1dd9b8d097a5" width=50%>  

##### _Selecting parts of an arm will allow you to change how that arm is controlled. Try selecting more bones to see what properties show up!_

# Available Rig-sets
The rigs start to differ when it comes to how you can control the face, where three unique ideas surfaced.  

All faces are controlled through Valve's [HardWare Morph](https://developer.valvesoftware.com/wiki/SFM/Introduction_To_HWM) system. In short, it realistically simulates how the face deforms through ~45 flex controllers.

- hisanimations' Rigs
  - Similar to SFM/GMod facial controls. Preserves the Flex Controller and HWM system.
- Eccentric's Rigs
  - Takes an industrial approach by overlaying control points onto the face. These points can be dragged to deform the face.
- ThatLazyArtist's Rigs
  - Takes an alternative approach by using a panel full of sliders to pose the face.  
## hisanimations' Rigs
hisanimations' rigs keep the original functionality of the face posing. I.E., preserving the way they were intended to be posed. It utilizes ~45 named sliders to manipulate the face. While the sheer number of sliders may be overwhelming to some, their names provide an idea of what they do. It's a good idea to get a feel for them. You filter out sliders based on Upper, Mid, and Lower sections of the face.

> [!NOTE]
> Suffixes such as `V`, `H` and `D` can be interpreted as `Vertical`, `Horizontal`, and `Depth`

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/f050d655-bb02-4e9d-8ab6-ce1e120b0dec" width=65%>

hisanimations' rigs are recommended for users switching from SFM or GMod.

## Eccentric's Rigs
Eccentric's rigs are recommended for new users, as they provide an intuitive and easy way to pose the face. Posing is done through moving the control points on the face.  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/e4568825-2157-4214-81fd-0cde82b45c0e" height=350>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/86cd8c5d-1e75-4faf-b531-ba69656086ff" height=350>

## TLA's Rigs
ThatLazyArtist's rigs take a more traditional path towards rigged face posing, by using a panel with sliders off to the side of the head. While the sliders themselves are blank, the name of every slider can be viewed on the top left corner of the screen.
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/212fbaf8-d271-43cf-87d0-4f12143b63b1" width=600>

# Features  
- All rigs have wrinkle maps to add details to the face.[^1]
[^1]:Wrinkle maps are calculated based on values of shapekeys, not how the mesh squishes and stretches.
- hisanimations' and ThatLazyArtist's rigs have shapekeys along with flex controllers to pose the face. This is a single slider solution to creating mouth shapes. These rigs are compatible with facial cosmetics.[^2]
- A QC eye shader was recreated to mimic the way Source engine eyes work. Eyeball meshes are not used.
- The mercenaries use TF2 style shading to look as close to TF2 as possible. [(Blender)VertexLitGeneric](https://developer.valvesoftware.com/wiki/Blender_VertexLitGeneric), rim lights and lightwarps have all been implemented.[^3]
- IK/FK swapping
- Legacy rigs for importing animations onto
- In-game and SFM versions of the mercenaries

[^2]:It's extremely easy to deform the face using shapekeys by activating two or more of them.
[^3]:The Cycles renderer does not support lightwarps. The albedo textures can be multiplied by vales ranging from two to four to approximate the correct shade the mercenaries tend to have.
