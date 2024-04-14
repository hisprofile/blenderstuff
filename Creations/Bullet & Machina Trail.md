# [Bullet & Machina Trail](https://github.com/hisprofile/blenderstuff/raw/main/Creations/blends/Bullet%20&%20Machina%20Tracer.blend)
[Bullet & Machina Trail (Download)](https://github.com/hisprofile/blenderstuff/raw/main/Creations/blends/Bullet%20&%20Machina%20Tracer.blend)

This has been recreated to look almost exactly like TF2. It uses simulation nodes and is dependent on the parameter `Activate` being set to `True` to fire.

There are a lot of parameters, so I'll only explain the ones that might raise confusion.

# Initializers
## Bullet Paths
Bullets will travel towards the direction the `Bullet Source` was facing at the time of activation. If you'd like to override the path in which they travel, define an object in `Bullet Endpoint` and enable `Use Bullet Endpoint`. This will force the bullet to travel towards the bullet endpoint at time of activation.

You may preview the bullet path by enabling `Preview Bullet Path`.

# Bullets
## Spread
Bullet spread is based on a factor of 0..1 ranging from 0 to 180°. 

## Travel
Bullets will travel at a constant rate, but the distance in which they travel is clamped to `Bullet Max Distance`. You can modify `Bullet Travel Speed` to multiply the rate at which they travel.

# Muzzle Flashes
`M. Flash Detail Count` determines how many instances make up the muzzle flash.

# Sparks
## Movement
`Sparks Random XY` determines the maximum distance they can travel on the `Bullet Source`'s X and Y axis. Same goes for the Z axis parameters, but it has a minimum and maximum value.

For the sake of organization, you may stack `Bullet Effect` node groups on a single object.

![image](https://github.com/hisprofile/blenderstuff/assets/41131633/ae8cf31f-bb65-4984-b8e9-872436b13d35)
