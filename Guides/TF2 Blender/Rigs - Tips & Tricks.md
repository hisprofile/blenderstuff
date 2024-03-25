# Rigs - Tips & Tricks  
Here's a list of tips & tricks you may find useful when working with the mercenaries.

## Scaling & Moving Eyes    
Eyes are a shader projected onto a strip of mesh from an object acting as an origin point. The objects in question are [Empties](https://docs.blender.org/manual/en/latest/modeling/empties.html). You can find these objects behind the eyes to move and scale to your liking.

By default, the eyes track the prisms (control points) on the rig. These prisms are parented to the pivot cross. Not only do they track the prisms, but they copy the scale as well.  

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/dff7279f-e345-4558-bc40-e6ed557645bf" height=320>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/f86fe125-ddfc-45fc-ac23-8fe691d708da" height=320>

To track other objects, such as cameras, locate the empties behind the eyes, and change the `Track To` target in the `Constraints` tab.

## Changing Eye Textures  
For a good texture swap, make sure it matches the proportions of the eye below. Then, swap the texture out for your own in the shader editor.  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/61840717-8783-4012-b6cc-52f3ceb56260" height=64>  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/265f7aa3-1ec8-400a-9ea6-c3467990c358" height=425>

## Custom Flex Tool (Sculpt Tool)  
The sculpt tool is an incredibly fun tool to use when working with the mercenaries, as it can add mass amounts of stylization. The best way to approach this is to add a new shapekey to the head, so the original face shape stays intact.  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/865e83d0-bb44-448a-bf8e-6879aca8dbcb" width=50%>  
Set the new shapekey's value to `1.0`, enter `Sculpt` mode and go crazy!  

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/038490c2-cca9-41bc-a493-a411002af69f" height=400>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/2ad8a43b-9463-4dea-8baa-9a1e586fb84c" height=400>

## How Facial Flexes Work  
The way facial flexes work on these models are truly an incredible feat. Each head contains 300+ shapekeys with every way the face can realistically deform. Then, all of these shapekeys are condensed down to around 45 [Flex Controllers](https://developer.valvesoftware.com/wiki/Flex_controller) through a series of mathematical expressions. The result is a realistic simulation of how a face moves.  

[Heavy's shapekeys and math expressions.](https://pastebin.com/DX6JsfzM)
