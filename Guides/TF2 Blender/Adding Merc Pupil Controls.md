# Adding Merc Pupil Controls
##### Written by [Katy133](https://www.youtube.com/@Katy133)

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/423a7811-3e14-41db-afd9-832344be3f74" width=30%> <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/932bfc64-a749-408b-92b2-a6a319cc6d14" width=30%> <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/38d25da1-e245-4967-aebc-fe7bad138800" width=30%>

In real life, the human pupil (the black dot of the eye) will dilate when a person is looking at something they like, and shrink when they are scared. Pupils will also adjust to dim and bright lighting.

In animation, animating the pupils' size can help elevate your animation acting, especially in extreme close-up shots that are emotionally-charged.

Example of pupils shrinking:  
<img src="https://64.media.tumblr.com/886efaa0047f41f3638cca441f32efd3/fdb0cfe89cf08734-b3/s1280x1920/b7082db5d47861964228ff56301c5ebf745d3297.gif">

Example of pupils dilating:  
<img src="https://i.giphy.com/Q6WPVzFU8LcBWWgQE1.webp">

Here is a guide by Katy133 on how to edit the mercs' eye shaders to allow you to control and keyframe the size of the pupils.

Making the pupils grow or shrink requires a different shader node setup for each. This guide will explain both, using Scout's SFM rig as an example.

# Pupils Shrinking Control 

Select the merc head model (the mesh) of the merc you want. In the Materials Property tab, select the material slot for the merc's eye material (example: `Scout left eye`).

Go to the Shader Editor. Select the `New Material` button (to the right of the material's name) to create a duplicate of the eye material. Rename this new material to something clear (example: `Scout left eye pupil_small`).

For this new material, add the following new nodes:
- Two Mix nodes set to Point.
- Two Color Ramp nodes set to Constant. Add a frame around one of them, and rename it `Pupil Shrink Control` to make it easy to find when you're animating.
- A Gradient Texture node set to Spherical.
- Two additional Mapping nodes.
- A copy/paste of the Image Texture node `iris_blue_l.png` (for Demoman, the texture is named `iris_brown_r.png`)
- Arrange these nodes to look like the screenshot provided below:

![image](https://github.com/hisprofile/blenderstuff/assets/41131633/4a4f9478-a5c9-4cc0-8b59-1fc7ae739e3b)


Depending on which merc you are working with, you will need to adjust the values of the two new Mapping nodes. Holding shift while adjusting the values will slow down the value shifting, which may help you get exact positioning you want. You're basically "eye-balling it" here.
- The mapping node to the left sets the centre of the gradient mask's centre (so adjust that one's XYZ Locations if the mask circle isn't centred right, and the XYZ Scale if the mask isn't big enough and is creating a "double-pupil" effect when the eye moves around),
- while the right Mapping node sets the position of the scaled up iris (so adjust that one's XYZ Locations if the shrunk pupil isn't centred right).

You have now created a material shader that basically adds two versions of the iris (the default one and a scaled up version) with a mask that lets you switch between the two. The mask is shaped like a circle, giving the illusion of just the pupil shrinking.

For the other eye:
- Follow the same steps for the other eye (example: `Scout right eye`).
- If you copy/paste nodes from the left eye to the right eye, make sure the Texture Coordinate's assigned Object and the Mapping node's values are correct (as these are different between the left and right eyes).

![image](https://github.com/hisprofile/blenderstuff/assets/41131633/2e2370bc-9747-4305-8ef8-befcf8502aea)


Note that you should NOT reuse the exact same pupil control shaders for each merc, as each merc uses custom adjustments to their respective eye shaders (for example, Sniper's TF2 Eye shader node has different values for `Sclera occlusion` than Scout. So giving Sniper Scout's eye shaders would make Sniper's eyes look off-model).

Also note that, due to the low poly style of merc models, the circle shape of the mask may be slightly angular. This is caused by a spherical gradient being applied to an angular shape (a low poly eye).

# Pupils Pupils Dilating (Making Bigger) Control 

Follow the same steps for creating the Pupil Shrinking Controls, but name the material appropriately (example: `Scout right eye pupil_big`), and make the following changes to the nodes:
- For the top Mix node, swap the inputs for the A and B values.
- Rename the frame around the Color Ramp node to `Pupil Grow Control`.
- For the two new Mapping nodes, change the values to look like the screenshot below:

![image](https://github.com/hisprofile/blenderstuff/assets/41131633/eae8a8f5-01ea-43b0-89d2-72759f0257b1)


Again, note that depending on the merc you are working with, you may need to adjust the values of the two Mapping nodes.

For the other eye, again:
- Follow the same steps for the other eye (example: `Scout right eye`).
- If you copy/paste nodes from the left eye to the right eye, make sure the Texture Coordinate's assigned Object and the Mapping node's values are correct (as these are different between the left and right eyes).

# Animating the Pupil 

- The Color Ramp node (the one directly connected to the Gradient Texture) is what you will use to animate the pupil's size.
- To do so, select the black control and move it along the slider until the pupil is the size you want it.
- To keyframe the pupil, right-click on the `Pos` value of the node and select `Insert Keyframe`. The value should turn yellow now. Yellow means the value has a keyframe on the frame you are currently on, green means the value contains keyframes on another frame in the timeline. You can also add a keyframe by hovering your cursor over the value and pressing the add keyframe hotkey.
- To make both the left and right pupils move the same amount at the same time, switch to the other eye's material (by selecting its material slot in the Materials properties tab) and inputting the same `Pos` value as a keyframe on the same frame.

### Relevant
You can control the total eye scale by scaling the eye target objects on the rig.
