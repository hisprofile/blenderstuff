# Shading - Tips & Tricks
## Pseudo Lightwarps - Cycles
In TF2, mercenaries, weapons and buildings use lightwarps to brighten up the model, helping create contrast between dynamic objects and the background. It also tends to give these things a brighter shade that we're used to. Without this shade, it just looks weird.

This is exactly what happens when you swap between EEVEE and Cycles. Lightwarps can be recreated in EEVEE but not in Cycles, so you'll see this shade change when you swap between the render engines. 

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/663e43f4-2a1d-45b1-ac7f-520dda6c79dc" height=300> <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/f7daf2c4-deb2-4080-8ffd-266eed592e3c" height=300>



The remedy is to multiply the albedo (base texture) by a value or color. You can use this node group I made to try to fix it!
