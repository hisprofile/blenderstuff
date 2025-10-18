# How to Update Eye Materials for TF2-Trifecta Mercenaries
## Fantastic News!
After four years, the mercenary eye shader has finally been updated to be ON-PAR with SFM! 🎉🎉

This replaces the dinky old shader that simply projected a texture onto the mesh. I have finally been able to read the original shader source code, and re-create the shader with Blender's shader nodes!

Getting this update is as simple as updating your TF2 rigs through the TF2-Trifecta. However, older projects will still use the original eye shader. Luckily, updating the shaders is no monumental task.

## Updating the Shader
After updating your TF2 rigs, your old projects should now have a text file named `source eye updater`, automatically imported via `_resources.blend`

<img width="70%" alt="image" src="https://github.com/user-attachments/assets/a809ef4c-e35a-4704-89cc-ada7375c1fdb" />

⠀  
After locating the text file, execute the script.  
<img width="397" height="48" alt="image" src="https://github.com/user-attachments/assets/d83e7115-31a2-41b5-b384-feb5f8b034a2" />

Then, go to the "Tool" tab, and locate the "Update Mercs Automatically" operator. Click on this operator.
<img width="546" height="506" alt="image" src="https://github.com/user-attachments/assets/f14d52f5-a469-4354-8c2d-9ca659a9ba58" />

Ta-da!!! Your mercenaries should now have the new eye shader.  

Before:  
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/6d61c74f-9fb9-4d36-9581-a05da2f69125" /> <img width="40%" alt="image" src="https://github.com/user-attachments/assets/a141f778-9ba2-492f-a3d4-460d00603a12" />

After:  
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/7b62d74a-55fc-473e-a453-4723d3970649" /> <img width="40%" alt="image" src="https://github.com/user-attachments/assets/5a7759a4-9fb5-417e-9ff1-8dfb5de3dcc5" />
