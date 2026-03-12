##### [Table of Contents](https://github.com/hisprofile/blenderstuff/blob/main/Guides/Rigi-All/Documentation/!Table%20of%20Contents.md)
# Miscellaneous Documentation
<img width="513" height="127" alt="image" src="https://github.com/user-attachments/assets/71216bc0-9de9-4471-9a48-2ecf22483f6d" />


> Rigi-All's different view modes, each with their own tools. Available in the viewport.

## Introduction
A set of tools separate from rigging, but can still be used with rigs.

## Miscellaneous Tools
### Make Bones Renderable
- Exclude Hidden Bones (parameter)
  - If enabled, it will not create objects for hidden bones.

Works best with Rigify rigs.
`Make Bones Renderable` copies the geometry and color for every bone shape, then converts it to a tube with geometry nodes that supports even thickness/miter edges. 

<img width=75% alt="image" src="https://github.com/user-attachments/assets/32823ad4-9491-4349-998a-61adbcac8f21" />

More properties are available in the geometry nodes modifier.
<img width=75% alt="image" src="https://github.com/user-attachments/assets/286b7ac5-abaa-48c7-9c4a-42928b5e89b4" />

### Visibility Switch Helper
Did you know you can have menu switches as custom properties? They're great for controlling the visibility of objects. For a rig, this makes showing/hiding detail groups very convenient.

To get started, gather objects that will have their visibility controlled. The active object will hold the visibility switch for the selected objects. When ready, just click `Add Visibility Switch`

<img width=75% alt="image" src="https://github.com/user-attachments/assets/e47a014f-fd84-456a-bbda-e8c6155566ad" />  
<img width="75%" alt="image" src="https://github.com/user-attachments/assets/5c09f7b5-9543-4e99-adce-ee345099b85f" />

<br>To build the switch, simply use the `Build Visibility Switch` operator.

<img width=75% alt="image" src="https://github.com/user-attachments/assets/a073a73c-e06d-41d1-9dd7-b9b193f0b944" />

Et voilà! You have a visibility switch as a custom property! Just so there's no confusion, users are not required to instal Rigi-All to use these visibility switches.

To control more than one object with a single visibility item, gather some objects, and use the <img width=20 src="https://github.com/Shrinks99/blender-icons/blob/main/blender-icons/restrict_select_off.svg"> Select tool to set multiple objects to a visibility item.

<img width=75% alt="image" src="https://github.com/user-attachments/assets/4e40fec0-4f86-46d7-a13b-a8afbb32aceb" />

<br>You can leave the object parameter empty, so you may use the switch to drive other properties instead of an object.
<img width=50% alt="image" src="https://github.com/user-attachments/assets/623b513c-9141-4443-86a4-6a9da17db4cf" />  
<img width=50% alt="image" src="https://github.com/user-attachments/assets/ee9038a0-496b-4561-a825-72170d624fa7" />  
<img width=50% alt="image" src="https://github.com/user-attachments/assets/30e9b46a-eb9b-4d46-8f5f-393c101652dd" />

# Other Links
- [Rigging](https://github.com/hisprofile/blenderstuff/blob/main/Guides/Rigi-All/Documentation/Rigging.md)
- [Clean Up](https://github.com/hisprofile/blenderstuff/blob/main/Guides/Rigi-All/Documentation/Clean%20up.md)
