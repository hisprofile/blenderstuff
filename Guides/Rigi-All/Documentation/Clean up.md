##### [Table of Contents](https://github.com/hisprofile/blenderstuff/blob/main/Guides/Rigi-All/Documentation/!Table%20of%20Contents.md)
# Clean Up Documentation
<img width="516" height="128" alt="image" src="https://github.com/user-attachments/assets/07c03e20-8d45-4f01-8fd7-a7a12bffb6c3" />

> Rigi-All's different view modes, each with their own tools. Available in the viewport.

## Introduction
A set of tools for cleaning up a rig before or after generation.

## Clean Up Tools (Post Rig Generation)
### Add "DEF-" to Vertex Groups
- Not required on an armature with preserved bones.

By default, the mesh will not follow the generated Rigify Rig due to having mismatched vertex group and bone names. 

Therefore, using this on all selected mesh objects will prepend "DEF-" to the required vertex groups, aligning the vertex groups with the armature.

### Remove "DEF-" from Bone Names
- Not required on an armature with preserved bones.

By default, the mesh will not follow the generated Rigify Rig due to having mismatched vertex group and bone names.

Therefore, using this on the Rigify Rig will remove the "DEF-" prefix on the required bones, aligning the bones to the vertex groups.

While it works, this option is *extremely* destructive to the rig and is not recommended. Use the former tool if possible.

### De-Duplicate Boneshapes
- De-duplicate Type (Parameter)
  - Only Clean Up Armature (default)
  - Clean Up ALL Shapes in Project

Every bone on a Rigify Rig has a unique bone shape object. While they are visually similar to other objects, they are indeed their own. This tool de-duplicates these bone shapes, so those that are visually similar are then made the same object.

## Clean Up Tools (Pre Rig Generation)
### Remove Unassigned Vertex Groups
- Only remove bone groups (Parameter)
  - Only affect vertex groups if they are associated with bones. Requires an armature to be referenced through an armature modifier.
- Remove groups with zero vertex weight (Parameter)
  - If disabled, it will only affect vertex groups with no vertices assigned to them.

    If enabled, vertex groups with zero vertices using them assigned or not, will be affected. This takes longer as a deeper search is performed.

Remove unused vertex groups.

### Remove unused Bones
- Remove groups with zero vertex weight (Parameter)
  - If disabled, it will only affect bone vertex groups with no vertices assigned to them.

    If enabled, bone vertex groups with zero vertices using them, assigned or not, will be affected. This takes longer as a deeper search is performed.

Remove unused bones.
### Remove Unused Bones & Vertex Groups
- Remove groups with zero vertex weight (Parameter)
  - If disabled, it will only affect bones & vertex groups with no vertices assigned to them.

    If enabled, bones & vertex groups with zero vertices using them will be affected. This takes longer as a deeper search is performed.

Remove unused bones and vertex groups.
# Other Links
- [Rigging](https://github.com/hisprofile/blenderstuff/blob/main/Guides/Rigi-All/Documentation/Rigging.md)
- [Miscellaneous](https://github.com/hisprofile/blenderstuff/blob/main/Guides/Rigi-All/Documentation/Miscellaneous.md)
