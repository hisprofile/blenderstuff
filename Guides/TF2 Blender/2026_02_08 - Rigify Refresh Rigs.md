![Render Result](https://github.com/user-attachments/assets/ea79e8e7-a859-41e2-9451-2d76f596b0d6)

# TF2 Blender: Rigify Refresh
## Introduction
The mercenary rigs have received a major overhaul, released as the "Rigify Refresh". These rigs are ready for modern Blender, and have brand new features with custom Python Tools. These features include, but not limited to:
- **New Eye Shader**
  - The eye shaders have been reworked to now appear visually similar to its SFM counterpart.
- **Iris Dilate Controls**
  - Bones that sit in front of the eyes can be scaled to dilate or constrict the iris.
- **Includes Prop Bones**
  - Rigs now have prop bones, which were previously lacking. This can help them be used for taunt animating.

The following are features accessible in the `Item` panel in the 3D viewport.
- **Bodygroup Controls**
  - New switches are introduced to change specific parts a mercenary. This mostly regards switching between the cosmetic-compatible TF2 bodygroups, and the higher-quality SFM bodygroups.
- **Swap Into DEF- Bones**
  - You can now choose to use the provided "Deform" bones in a rigify rig, which may have better deformations.
- **Swap Bone Matrix Types**
  - You can now swap bone configurations, between what is compatible with TF2, and what is compatible with SFM imports/exports. Using SFM mode may result in badly-deformed cosmetics.
- **Snap Rigify to FK Pose**
  - By bone-merging a Rigify rig to an animated legacy FK rig, you can use the `Snap Rigify to FK Pose` tool to copy the pose onto the Rigify rig. This makes it extremely easy to animate off of game animations for the sake of continuity, as you may release the bonemerge influence whenever you need.
- **Direct Export to .DMX animation**
  - The `Quick Export to DMX` tool will go through the scene frame range, preview or not, and export the Rigify animation as a .dmx animation. This can then be imported into SFM. **Make sure the matrix type is in SFM mode!**

There are rigs for 4.5 and older, and rigs for 5.0 and newer. The newest rigs will be taken care of the most. Eccentric's and TLA's rigs will not receive this update.

Use these rigs with the latest version of the TF2-Trifecta!

[Rig Downloads](https://drive.google.com/open?id=1DF6S3lmqA8xtIMflWhzV242OrUnP62ws&usp=drive_fs)
## Feature Documentation
### Swap Into DEF- Bones
The `Swap Deformation Type` tool can swap usage between the original rig for deformation, and Rigify's Deform (DEF-) bones. Using "Better Deform" can result in better deformations and grants more options given by Rigify's properties.

> ( Default Deform, Better Deform. Notice how the rotation blends down the arm on Better Deform. )

<img width="45%" alt="image" src="https://github.com/user-attachments/assets/26401842-759e-46ec-85cf-50e2935fdc70" />  <img width="45%" alt="image" src="https://github.com/user-attachments/assets/f968b642-2047-4e04-9483-0c30358cb874" />

### Snap Rigify to FK Pose
This requires a Rigify rig and a Legacy FK rig. The latter can be spawned alone by holding `SHIFT` while spawning a mercenary.

<img width="65%" alt="image" src="https://github.com/user-attachments/assets/f69fe5d9-ed4b-459c-9435-21792bc707c9" />

The following example will use the "Boston Breakdance" taunt from TF2.  
[Read this to learn how to import game animations into Blender](https://s2b.readthedocs.io/en/latest/TF2Vanilla/Animations.html)

<img width="65%" alt="image" src="https://github.com/user-attachments/assets/4c591c27-9905-4f85-bcf3-afa73e2b30b9" />  
<img width="65%" alt="image" src="https://github.com/user-attachments/assets/fdd280a1-65d8-436f-a099-4a7be9528b11" />

Then, using the TF2-Trifecta's bonemerge tool, merge the Rigify rig onto the Legacy FK rig. The corresponding, "overlaying" bones on the Rigify rig will then move to copy the Legacy rig.

<img width="65%" alt="image" src="https://github.com/user-attachments/assets/27949f69-2bb4-419b-933f-f364ef3fac48" />

Use the `Snap Rigify to FK Pose` tool to copy the Legacy FK pose onto the Rigify rig.

<img width="65%" alt="image" src="https://github.com/user-attachments/assets/02b10d14-0fcc-4a61-a940-009d7023aa84" />

Finally, manually snap the IK limbs to the FK limbs using Rigify's built-in tools, and change the limb mode to follow IK. This step is optional, and can be done on all arms and legs.

<img width="65%" alt="image" src="https://github.com/user-attachments/assets/b4e5cbe9-e1db-4597-ad9d-6533b843484f" />

There you go! A neat pose to animate from, and it was super easy to do! This can also be done with [animations imported from gameplay](https://www.youtube.com/watch?v=R_nCWv-vKg8). However, you may have to bonemerge in this order: Rigify rig > Legacy FK rig > gameplay rig

### Swap Bone Matrix Type
For some reason, animations exported from SFM have weird properties. On some bones, the rotation matrix items are shifted in their rows one place to the right. When imported, the matrices are unshifted. This does not happen when reading animation data directly from a .dmx session. The result are limbs that appear severely deformed.  

At any rate, it is not convenient to read the animation data from the .dmx session. So for the sake of convenience, you can change the bone configurations of the rigs on the fly to be compatible with SFM. This is available on both the Rigify rigs and the Legacy FK rigs. When in SFM compatibility mode, cosmetics will not be supported.

This will not alter the appearance of the mercenary. It is only for handling files that SFM imports/exports.

### Export to .DMX Animation
The `Quick Export DMX` tool will export animation from a Rigify rig to a .DMX file, which can then be imported into SFM. This utilizes the overlaying bones from the original rig. The rig must be in SFM compatibility mode, which you can activate in `Swap Matrix Type`.  

The animation start and end entirely depends on the scene's frame start and frame end. It also supports preview range.

<img width="65%" alt="image" src="https://github.com/user-attachments/assets/cbd221c3-56dd-46f0-8b55-734e2c9f6373" />
