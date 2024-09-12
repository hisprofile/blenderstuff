# Overview
These are a collection of files to help users piece together data from an SFM session in Blender. All scripts require the dmx_parser.zip addon to be installed into Blender, as it handles loading the .dmx session into memory.

Please remember that this is a working concept. I do not have the time nor skills to work on this further, so the project will be handed down to REDxEYE, the developer of SourceIO. All of this is still very limited.

datamodel.py in dmx_parser.zip was modified by Gorialis (https://github.com/Gorialis, https://www.youtube.com/channel/UCmYcXOW2QtwCRHpWQN4jxtg) for better consistency in loading times. Huge thanks to them!

# NOTES:
## dmx_parser.zip
- Install this addon into Blender.
- With dmx_parser, you can load most .dmx and .pcf (particles) files and view its data with the element tree mock-up. This element tree is only viewable in the Text Editor or Shader editor. Note that it does not port .pcf files, but lets you look at the data within to better help you understand how its composed. This is how I've recreated most particles.
## session_importer.py
- session_importer.py requires SourceIO to be installed as an addon. It will call the mdl importer tool to cache imports and animate them.
- session_importer.py does not import maps, but it does however create a collection named "map". Users are required to import the map themselves, and assign the imported data to this "map" collection.
- session_importer.py will only animate location and orientation on bones and objects. Scaling animation has not been implemented yet. It will also animate camera data, such as FOV (lens), aperture, and f-stop.
- session_importer.py does not animate shape keys, as Source Engine uses a vastly different shape key system than Blender.
- session_importer.py does not import .pcf files.
- session_importer.py does not animate skins or bodygroups
  - It will merge bodygroups, but they can be later separated through the Body Group Selector node group found in the _resources.blend file of any archive in the Source Engine Blender Collection (https://github.com/hisprofile/blenderstuff/blob/main/Creations/Source%20Engine%20Blender%20Collection.md)
- To use this script, load the .dmx file using dmx_parser, set your SFM game path to the `sfm` variable (second line), and run the script.

## getFace.py
- getFace.py only animates the faces on my TF2 mercenary ports, or anything following the HWM control scheme I've implemented in Blender.
- To use this script, set the shot, the track group, and the track object that the animation set is supposed to use.

## getBones.py
- getBones.py will bring over animation onto a ported model.
- To use this script, set the shot, the track group, and the track object that the animation set is supposed to use.

Download the tools (free): https://ko-fi.com/s/d349b3dd3f
