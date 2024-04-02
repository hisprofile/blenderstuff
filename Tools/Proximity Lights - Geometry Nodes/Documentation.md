# [Proximity Lights - Geometry Nodes](https://github.com/hisprofile/blenderstuff/raw/main/Tools/Proximity%20Lights%20-%20Geometry%20Nodes/geonodes_proxlights.blend)
This is a geometry nodes version of my tool, `Proximity Lights.` It hides lights far away and/or out of view from the camera. This is most useful for EEVEE Legacy, but I'd imagine you'd find use for this in Cycles and EEVEE-Next.

4.1+ only.

![image](https://github.com/hisprofile/blenderstuff/assets/41131633/fb9ebd99-ee97-4814-99dc-ee7c3135c75c)


## New vs. Original
This is *extremely* fast and real-time compared to the original version, at the cost of flexibility. The Original (python) version of the tool allows you to change properties of the lights while the tool is in use, such as brightness, color, and position. It will also ignore any sun lights automatically. The geometry nodes version requires you to instance a collection of lights then hide said collection to effectively use the tool, adding a roadblock to editing the lights. If you're looking for performance, the geometry nodes version is probably your best bet.

## How to Use
Append the node group named `Proximity Lights - GeoN` into your scene from the .blend file. Create an object (like a cube) to use as a source for the Proximity Lights tool. 
> [!TIP]
> Name it something good, and put it somewhere easy to access!

Add a `Geometry Nodes` modifier and set the node group to `Proximity Lights - GeoN.` Select a collection of lights to optimize. Take any lights you'd like to remain active out of said collection, like sun lights. Once a collection has been set, exclude it from the view layer through the check box.   

> [!WARNING]
> It's good practice to avoid leaving both the collection and the tool's object source active at the same time!

## Parameters
- Enable
  - Disable or enable light optimization.
- Collection
  - The collection of lights the tool will go through and optimize.
- Max Distance
  - How far away lights can be from the camera before they get hidden.
- Camera Frustrum
  - When enabled, anything out of the camera's view plane will be hidden.
- Light Culling
  - Set a hard limit to how many lights can be active at once.
