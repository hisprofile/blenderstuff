# Intro

Team Fortress 2 x Blender is undoubtedly a match made in heaven. With TF2's unique artstyle and Blender's ability to manipulate anything, a good art piece is always at your grasp. If people can get away with what they do on SFM, imagine what can be done in Blender. But hold your horses!! Don't get too carried away with whatever you're thinking- Remember that TF2 content was never meant for Blender. While it may be possible to get the results that you want, there's things worth noting for your new adventure.

<img src="https://github.com/user-attachments/assets/95aa5a8f-8921-4da2-9f70-cc1dfb857f12" width=60%>  

<sup>Image credits: [Katy133](https://www.youtube.com/@Katy133)</sup>

# Comparison
Let's compare SFM and Blender.

## SFM
Source Filmmaker is an animation program- that's it. There are no tools for modeling, texturing, or sculpting. However, that isn't a problem because of its workshop feature. Users have access to a wide array of User Generated Content to help them create.

While it is an animation program, it also has an extremely extensive particle system for quick, good-looking effects that requires almost no experience to setup.

Source Filmmaker is simple and caters to the users by having many built-in tools for their needs.
<details>
  <summary>Pros & Cons</summary>

### Pros
- Workshop
  - Thousands of UGC at anyone's disposal
- Streamlined for animation
- Good ratio between scene detail and program performance
  - Because SFM runs off of the Source game engine, everything is more realtime due to having model, lighting, and material data pre-baked, saving tremendous amounts of calculations from being performed.
- Realtime motion paths
  - Blender doesn't have that!
- Quick rigging tools for types of armatures (rigs)
  - It's a matter of clicking an item from a menu to rig a character with Inverse Kinematics.
- Good for old PCs
### Cons
- Extremely outdated
  - Uses Python 2.7
  - 32 bit program (limited to ~3.5GB of RAM!)
  - Very prone to crashing and visual issues
  - Limited rendering options
  - Uses 2007 TF2 (better than nothing I suppose)
  - Entirely reliant on community to workaround issues (respect+)
- Hassle to port
  - Bringing models into SFM can be such a hassle due to:
    - Compiling to .mdl, requiring a prepared .qc file
    - Converting textures to .vtf format
    - Writing materials
    - Requires specific folder structure
  - If they started in Blender, why not keep them there?
- Extremely limiting
  - Making custom shape keys on demand is impossible
  - Adding single images requires making a mesh plane then porting it to SFM

</details>

Summary: SFM is an outdated program streamlined for animation, and that's all you'll get. Compared to Blender, it's able to display more detail at higher performance simply because it runs off a game engine. It is not a true 3D generalist program, so you miss out on many features, but it still comes jam-packed with its own. And because it uses a game engine with 20 year old code, it can run better on older systems.

## SFM for Team Fortress 2
<details>
  <summary>Pros & Cons</summary>
  
### Pros
- Team Fortress 2 content is native to SFM
  - Everything works and looks how it should. Face posing, character shaders, particles, maps
- Easy to rig with IK
- Good ratio between scene detail and program performance
  - TF2 maps can be extremely detailed. Achieving an accurate result in Blender requires many workarounds and affects performance. Of course, this is no issue for SFM.
- Particles galore
  - The one thing Blender doesn't have...
- Built-In action recorder
  - Records your gameplay with ease
- Easy ragdolls
- Great eye shader
- Realtime motion paths
### Cons
- Limiting
  - You cannot make custom face shapes
  - You cannot easily change the lighting on a map
  - You cannot easily edit a material
- Sentries suck
- Map lighting is permanent

</details>

Summary: Everything works like it should, everything looks how it should. Valve animators use SFM for TF2 animations, and so do you. But with such a fun artstyle, what's the point if you can't push it to its limits? Also particles. Big win for SFM.

## Blender
Blender is an "everything" program. Everything you see can be changed one way or another, and I mean everything. And with its Python front-end, it's safe to say that Blender can actually do everything. (I made it control a robot arm!)

Blender is extremely reliant on its community. It doesn't lean towards compatibility with anything but the industry standards. Anything you want done will most likely take some addons to bridge a gap, whether it be porting, rigging, free asset libraries, tools, etc.

Blender is an advanced program that pushes the users to help themselves.
<details>
  <summary>Pros & Cons</summary>
  
### Pros
- Unbelievably versatile
  - If this were a swiss army knife, it'd be one you see in a cartoon. It's ridiculous what this program can do.
- Realtime rendering engine
- Raytracing rendering engine
- Good keyframe graph editor
- Great for stylized art pieces
- Great media exporter
- Constantly updated
- Open source
- Geometry nodes
  - Geometry nodes can literally do anything its crazy
- Modular
- Python front-end
### Cons
- Steep learning curve
  - There is so much to learn, but don't be thrown off by how tall the mountain may seem. Slowly but surely, you'll scale it. From moving a vertex, to shading a sphere, to simulating fluids and gasses, you can master it all.
- Requires newer hardware to run

</details>

Ever wanted to feel like Tony Stark? Mastering Blender has you feeling like that.

## Blender for Team Fortress 2
<details>
  <summary>Pros & Cons</summary>
  
### Pros
- Very flexible
  - You can sculpt your own faces onto the mercenaries
  - You can change the lighting on any map
  - You can make stylized shaders with the Shader Editor
  - You can make your own effects
  - You can live edit textures
- Great lighting tools
  - Make lighting your own with Blender's four light types: Point, Sun, Spot, or Area
- Drag 'n' drop assets
  - With Blender's Asset Library tool and the Source Engine Blender Collection, there's no need to preview and confirm loading a model. Just drag 'n' drop into your scene!
- HWM Face Posing
  - Face pose just like you can in SFM!
- Custom rigging tools
  - With constraints (condition/operation-based transformation) idk
- Tons of modifiers
  - With geometry nodes, the build tool, and [much more](https://docs.blender.org/manual/en/latest/modeling/modifiers/index.html), the need to re-export a model for a simple adjustment is GONE.
- Better media exporter
- Better rigs
### Cons
- Approximation is the best we have
  - Team Fortress 2 was never meant for Blender. That means everything needs to be approximated. Maps, facial movement, shaders, you name it. Someone can do a large part of the work, but it may be up to you to clean up the last details.
  - Things that were approximated
    - Lightwarps (gives the distinct toon shading we see on mercs), only in EEVEE
    - VertexLitGeneric shaders (mercs, props, cosmetics, weapons)
    - Map lighting (better in Cycles)
    - Eye shaders
- No particle support.
  - This is the most painful part. Particles have ZERO support in Blender. However, it is absolutely possible to recreate them using geometry nodes by parsing and reading the data of the .pcf file yourself and piecing it together. See [my particles](https://github.com/hisprofile/blenderstuff/tree/main/Creations)
- HWM Face Posing
  - This is mentioned twice, because the way it is currently implemented may not be the most efficient but it may be the only way. Mercenary faces comprise of 300+ shape keys to deform every part of the face. These shape keys can then be controlled with ~50 flex controllers through a series of long math expressions. It's almost a mathematical simulation of facial muscles contract to make a face. These hundreds of math expressions update whenever they can, which can truly hurt performance.
- Map detail, such as grass planes, light cones, sprites, and more are lost.
</details>
Summary: It can be *really* fun to animate TF2 stuff in Blender. With the tools to create a true cinematic experience out of wacky animation, what could possibly go wrong?

However. Blender really is a program that pushes you to do more on your own. Compared to SFM, it's higher maintenance, which tends to drive people away. But I encourage you to go out and search for tools to truly revolutionize your experience. Blender can stick with you your whole life, and it just might change it. Join the TF2 Blender Community and go through our community workshop! Our tools and ports just might inspire you to upload your own, truly making your home.

## SFM vs. Blender - Summary
All in all, you're giving up some old toys to play with some new toys. Just because TF2 stuff wasn't meant for Blender doesn't mean it cannot work. If you're coming from SFM, you might find it difficult that your workflow is incompatible with Blender, but giving it time can really open your eyes.

# What's been ported?
- [TF2 Collection](https://drive.google.com/drive/u/1/folders/1W0aNvtbGdBOdObtBBh7nsz9w661E6P_j)
  - Cosmetics
  - Weapons
- [Engineer's Buildings](https://github.com/hisprofile/blenderstuff/blob/main/Guides/TF2%20Blender/Buildings.md)
- [Mercenaries](https://github.com/hisprofile/blenderstuff/blob/main/Guides/TF2%20Blender/Rigs.md)
- [Maps, props, materials](https://github.com/hisprofile/blenderstuff/blob/main/Creations/Source%20Engine%20Blender%20Collection.md#team-fortress-2)
