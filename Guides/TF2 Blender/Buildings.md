# [Buildings](https://drive.google.com/drive/u/1/folders/11vyl_97Xy8LE-VPECfLlJ876poRZp6AT)  
[Download link](https://drive.google.com/drive/u/1/folders/11vyl_97Xy8LE-VPECfLlJ876poRZp6AT)  
All of engineer's buildings have been ported and rigged for cinematic purposes.

# Sentries  
Sentries are now fun to use and animate. Instead of rotating them towards a target, you can place a target anywhere and the sentry will automatically face said target. Also, changing the color of a laser no longer requires setting any kind of origin point! ;)  

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/567e40d0-66c2-4e15-9c65-fab97d43bb72" height=400> <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/b29ec75a-39d8-4674-a9c9-e215d8eaa454" height=400>

## Features  
- Target pointing
  - Each rig has a cross that the sentries point to.
- Tilting
- Muzzle Flashes
  - Muzzle flashes are rigged by dragging a slider shaped like a cone from left to right. The muzzle flashes are adjustable in width, length, and particle count, and can be adjusted when selecting the muzzle flashes.
- Togglable sappers and sapper outlines through sliders
- Dimmed shield and togglable laser through wrangler slider
  - Shield particle properties can be adjusted in the modifier panel. Activate wrangler to show shield to be able to select the shield.  
    <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/484099b8-909f-4b5e-baa2-187d3c067b49" height=300>  
- Firing animations
- No Ammo animations
- LVL. 3 Sentries with IK rocket heads
- Building animations
  - Done through dragging a slider
 
# Dispensers  
Nothing new, but dispensers are here. Setting the metal amount only requires dragging a slider

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/6ebe1fb3-b619-43f8-b6e5-bb2e4baa7d00" height=400>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/c8f4e989-274b-4e69-803b-52308af8380d" height=400>

## Features  
- Togglable sappers and sapper outlines through sliders
- Metal meter adjustable through sliders
- LVL. 3 animated dispenser pulse
  - Speed can be adjusted in modifiers panel upon selecting a dispenser
- Building animations
 
# Teleporters  
Teleporters have been rigged the simplest they can be. Spinning can be procedural or animated.

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/b610c8ed-a604-47cd-af4a-851f85e8d2c9" height=380>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/e9ce1d68-58c4-4d57-a2cc-8c00ac5b4bd7" height=380>

## Features
- Adjustable teleporter field through slider
- Adjustable teleporter charge through slider
- Togglable sapper and sapper outline through slider
- Building animations
  - Done through dragging a slider
- Togglable teleporter arrow (Entrance only)
- Two ways of animating teleporter
- Self-animated teleporter rings. Properties such as ring count and speed can be adjusted in the modifier panel. `Teleporter Field` must be activated.
  1. Nonlinear Animation Editor
      - Actions named `Recharge Lvl. 1/2/3`, `running`, `SpinDown` and `SpinUp` can be added to the teleporter's rig to animate the teleporter. This method is FPS locked and the speed will vary.
       <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/0027d087-168d-477b-815b-0e6b42a03c44" height=200>
       <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/6382d745-ab2f-4d09-86ab-5296ff10efdc" height=200>
  2. Geometry Nodes, Procedurally (Recommended)  
      <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/f47ee869-f0dd-4fcf-bc84-5caf5f087f40" height=250>  

      - A geometry node group named `Teleporter Procedural Spin` has been added to spin the top of the teleporter. This method is not FPS locked and speed will remain constant. This method is recommended as the spinning behavior is similar to the game. Adjusting speed is done through `User-Defined Speed` or `Preset Speed`. `Preset Speed` has six different speed options available.

        The transitioning between differing speeds can be adjusted through `Transition Mix`.
        
        If you use this method and want to keep the teleporter blur object, then hide or delete the trails that activate through the `CHARGE` slider as the trails are included in the node group.
