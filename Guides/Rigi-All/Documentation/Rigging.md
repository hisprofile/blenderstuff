##### [Table of Contents](https://github.com/hisprofile/blenderstuff/blob/main/Guides/Rigi-All/Documentation/!Table%20of%20Contents.md)
# Rigging Documentation
<img width="517" height="130" alt="image" src="https://github.com/user-attachments/assets/7b68b437-e1c7-451f-90d2-8523fd52ea2d" />  

> Rigi-All's different view modes, each with their own tools. Available in the viewport.

## Introduction
To make rigging as easy as possible, prepare your model with a checklist to make sure everything is in order.

### The Check List
1. Make sure the Rigify add-on is enabled!
2. Ensure your model is standing up and facing the -Y axis. With this orientation, the right side of your model should coincide with the -X axis.
   - Don't forget to apply rotation if you have to make changes!
3. (Optional) Trim away unused data from your model. In Rigi-All's `Clean Up` tools, you can use the `Remove Unused Bones & Vertex Groups` tool (with the armature selected). This can clear any clutter that might get in your way later.
4. Initialize the rig in the `Rigging` tools. This allocates bone collections and color groups for the final Rigify rig. A "finalization" script is also attached.
   - If enabled, the `Preserve Original Bones` parameter will keep the original bones untouched, but give you a copy of each one to build the Rigify rig with.  

     Potential use cases are exporting animation data from the skeleton, or bone-merging accessory items to the rig, which require the original bones.

     As a drawback, you will be unable to use the "DEFORMATION" bones of the Rigify rig. Use wisely.
5. Ensure bones are symmetry compatible. Once initialized and in `POSE` mode, you will have access to the `Fix Symmetry Name` tool.
   - Do not use if your bones already end in any combination of `_, ., -` followed by `l, L, r, R`
   - As an example, `bip_upperArm_L/R` is compatible with symmetry, whereas `bip_L/R_upperArm` is not. To be able to use symmetry posing, your bone names will have to be formatted if their case is similar to this example.
  
     In the `Fix Symmetry Name` tool, set the `Left & Right Symmetry Keyword` parameters to `_L_` and `_R_` respectively. After executing `Format Names`, your bones will be formatted to `bip_upperArm.L` and `bip_upperArm.R` respectively, and are now symmetry compatible.

     Rigi-All's limb generation tools allow you to select one limb, and make a Rigify limb out of both sides. If you do not format names correctly, you will not be able to use this!

<br><br>Congratulations, pilot! You've made it through the checklist. You're ready to fly!

Read through the rigging tools to learn what's at your disposal.
## Rigging Tools
### Auto-Complete Other Side Feature
Rigi-All lets you select a chain of bones on one side, so it can generate a limb for both sides. In order to use this feature, make sure your bones are symmetry compatible!

### Bone Rolling
The `Bone Roll` tool rotates any selected bone by -90° or 90°, on its local X, Y or Z axis. Together with the `Show Axes` option enabled in the armature data tab, orient your bones to make sure the tails of bones point to the heads of their children.

In an ideal setup, your bones should perform their natural rotation on their local +X axis. To check multiple bones at once, use the "Individual Origin" pivot point.

### Make Arms
- Requires 3 selected bones per chain

Creates a Rigify Arm out of the selected chain of bones.

> [!IMPORTANT]
> If the IK arms "freak out" in the generated Rigify rig, ensure your upper and lower arm bones are *NOT* in a straight line. In edit mode, nudge the elbows back if you need to.

### Make Fingers
- Requires at least 2 bones per chain. Select however many chains as you'd like.
- Primary Rotation Axis (Parameter)
  - Automatic
  - -/+X manual (+X default)
  - -/+Y manual
  - -/+Z manual
- IK Fingers (Parameter, True or False)

Creates Rigify Fingers out of multiple selected chains.

### Make Legs
- Requires 4 selected bones per chain

Creates a Rigify Leg out of the selected chain of bones.

> [!IMPORTANT]
> If the IK legs "freak out" in the generated Rigify rig, ensure your upper and lower leg bones are *NOT* in a straight line. In edit mode, nudge the knees forward if you need to.
For simple legs that only consist of three bones with no toe bone, simply extrude a bone to act as a toe. 

### Make Spine
- Requires a chain of at least 3 selected bones.

Creates a Rigify Spine out of the selected chain of bones. By default, the pivot position is set at its lowest.

### Make Neck/Head
- Requires a chain of at least 2 selected bones.

Creates a Rigify Super_Head out of the selected chain of bones.

### Make Shoulders
- Requires 1 selected bone. No chain.

Creates a Rigify Shoulder out of the selected bone.

### Make Generic Chain
- No limit on selection
- Rigify Type (Parameter)
  - Choose any Rigify type to apply on the selected chains.

Automatically connects the selected chains of bones, and applies a Rigify Type if the parameter is set.

### Make Extras (Automatic)
- Widget Shape (Parameter)

This should be done last. It will mark any bone that was not a part of any limb generation as an Extra bone. These bones will carry over into the generated Rigify Rig.

### Make Extras (Only Selected)
- Widget Shape (Parameter)

Marks the selected bones as Extra bones. These bones will carry over into the generated Rigify Rig.

# Other Links
