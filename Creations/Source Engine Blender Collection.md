# Portal 2
## Tips
### 4Panels
It seems that panel arms (I don't know what they're called) don't move the panel they are attached to automatically. It seems the solution is to close it using its close action, select the panel, then parent it to one of the moving bones. `props_ingame/arm_4panel/@ramp_90_deg_close` seems to work.  

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/d7381a85-3479-4a28-8377-794067c04bb8" width=40%>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/e316b170-01d4-498c-9647-200096bb6380" width=40%>
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/aeaa8f3e-5c67-4164-81cb-d643e291f499" width=40%>

## Effects
### Hard Light Bridge
Prop `props/wall_emitter` has a geometry nodes effect linked as a custom property. To use it, add a geometry nodes group and set the node group to `Hard Light Bridge`
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/0510ea5d-c192-4a04-9890-d6086b1d4094">
