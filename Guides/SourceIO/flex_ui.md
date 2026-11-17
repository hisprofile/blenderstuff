# SourceIO for Blender - Flexes
## Introduction
SourceIO's .mdl loading has been overhauled to preserve more data from an .mdl file. This includes:  
- Flex Controllers
- Flex Expressions
- Flex Stereo Weight Balance (the vertex mask used to separate the left and right face)
- Wrinkle Maps

This guide aims to help you understand how these features work and how to use them in the UI.

## Importing
<img width="25%" alt="image" src="https://github.com/user-attachments/assets/851c1f85-0567-47d8-86aa-02321461c905" />  

> Import options for the .mdl importer.<br>

When importing with `Create drivers for flexes` enabled, SourceIO rebuilds the facial control scheme in Blender through a series of drivers and custom properties.

Custom properties act as flex controllers and are placed on the mesh data-block.

<img height="600" alt="image" src="https://github.com/user-attachments/assets/7276f4a8-7294-4001-9e58-c1e7f33dc36a" />
<img height="600" alt="image" src="https://github.com/user-attachments/assets/bcc0891c-aa02-40fd-8d82-060e1312cabc" />

> Shape keys with drivers and the flex controllers (stored as custom properties) that control them.

Flex controllers provide an understandable interface to control the face. Because custom properties are drawn in alphabetical order, a prefix is used to help them keep their order. "aaa" is 000, "aab" is 001, and so on.

aaa_fs is always the first flex controller, and acts as a Flex Scale control to multiply the final result of the face.

Custom properties are used to simplify the share-ability of the model.

## Flex Controller UI
<img width="500" height="492" alt="Untitled" src="https://github.com/user-attachments/assets/34b95628-cc15-4b2a-8a18-1f1d2420264d" />

> An example of the Flex Controller UI

The behavior of the UI is closely patterned after SFM's UI behavior. Because of UI restrictions in Blender, this behavior may confuse users.

Each flex UI controller is drawn with its _value_, a <img height="26" src="https://raw.githubusercontent.com/Shrinks99/blender-icons/e00f65a942cdd66206bdb454e33798b4199a6ae3/blender-icons/keyframe.svg">_keyframe button_, and a <img height="26" src="https://raw.githubusercontent.com/Shrinks99/blender-icons/e00f65a942cdd66206bdb454e33798b4199a6ae3/blender-icons/restrict_view_off.svg">_value viewer toggle_.  

When the _Value Viewer_ is <img height="26" src="https://raw.githubusercontent.com/Shrinks99/blender-icons/e00f65a942cdd66206bdb454e33798b4199a6ae3/blender-icons/restrict_view_off.svg">enabled, the custom property values are drawn. Default option for mono/single flex controllers.

When the _Value Viewer_ is <img height="26" src="https://raw.githubusercontent.com/Shrinks99/blender-icons/e00f65a942cdd66206bdb454e33798b4199a6ae3/blender-icons/restrict_view_on.svg">disabled, the Flex UI Controller is drawn instead. Default option for stereo/dual flex controllers.

Flex UI Controllers can drive one or two flex controllers at the same time, and uses a unique type of slider. Its values are **purely additive**, and will **reset to 0.0** upon release! For Stereo Flex UI Controllers (like smiling), the value of the Left/Right balance is multiplied onto the Flex UI Controller's value and applied onto the face.

**Again, Flex UI Controller values are additive. They will not retain their value in the UI, but their effect on the face will be saved.** These were specially developed to write to two other values at the same time, but not to read from them.

## Wrinkle Maps
<img height="500" alt="image" src="https://github.com/user-attachments/assets/03a43032-c3ee-4a65-977e-fb8ebb3c27bb" /><img height="500" alt="image" src="https://github.com/user-attachments/assets/d58c3397-d2b6-4883-b3ec-3f3cf64f5d2e" />

> First image shows the result of incorporating wrinkle maps. Second image shows the wrinkle map attribute.

When importing a supported .mdl file with `Generate Wrinkle Map Nodes` enabled, wrinkle map data will be reconstructed using geometry nodes and drivers. This data gets saved as an attribute named "tension" which can be used in the Shader editor.

Disabling this geometry node modifier in the viewport can improve performance.

## Debug Stereo Flex Balance
When this import option is enabled, the stereo balance is not baked into the shape keys. Instead, it is saved as two distinct vertex groups named "blendleft" and "blendright". These vertex groups are then used to mask the shape keys. You may adjust these masks in Weight Paint mode.
