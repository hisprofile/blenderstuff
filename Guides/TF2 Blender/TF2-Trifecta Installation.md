# Installing the TF2-Trifecta
After downloading the [latest version](https://github.com/hisprofile/TF2-Trifecta/releases) of the addon (Don't extract!), you'll want to head towards Blender's preferences by going to `Edit -> Preferences -> Add-ons -> Install...` to install it into Blender.  

Locate the newly downloaded .zip file, select it and choose `Install Add-on`. In a moment's notice, the TF2-Trifecta will be installed into Blender. Now, the only thing left is to install the assets used by `Wardrobe` and `Merc-Deployer.`

# Installing Assets
### Requires 4GB of free space!
### Both methods use Google Drive to download from, as I don't know of any straight forward, cheap file hosting services. If you know of one that requires no API to download from, then don't hesitate to reach out. If you are being withheld from downloading by a rate limiter, then you have my sincerest apologies. I have no alternatives.

### Method #1
The easiest way to install the assets is by going into the `Scene Properties` and using the `Install TF2 Collection` feature with `Include Rigs` enabled. Set the installation path to an empty folder and begin.  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/9ac28e55-852a-4af0-9123-a86a25dd1433" width=40%>
Within a short wait, the TF2-Trifecta should have automatically installed all the required cosmetics, weapons, and rig assets, allowing you to now utilize all features of the TF2-Trifecta including weapon/cosmetic spawning, cosmetic painting, and mercenary deployments.

### Method #2  
If for whatever reason you \**don't*\* choose the easy way and want to download the assets one by one, then here's the guide for that, I guess.

Open [The TF2 Collection](https://drive.google.com/drive/u/1/folders/1W0aNvtbGdBOdObtBBh7nsz9w661E6P_j) folder in Google Drive, and download the whole thing as a `.zip` archive. The `.zip` download will be split, but don't be concerned. It's fairly easy to extract and it helps prevent crossing a rate limiter threshold.  
Once the `.zip` files are downloaded, move them where ever you'd like. Select all the .zip files, right click on one, and press `Extract All`. Doing this should result in a complete download of all the assets with their original folder tree intact. If you encounter any failure in the future regarding these assets, then you most likely did not extract them correctly or successfully.  
With all the cosmetics and weapons downloaded, it's now time to download a [Rig-set.](https://drive.google.com/drive/u/1/folders/1DF6S3lmqA8xtIMflWhzV242OrUnP62ws) Read the guide on rigs to choose which rig-set is right for you.  

With the cosmetics & weapons downloaded, your folder structure should look like this:  

<details>
<summary>File Paths</summary>

<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/90025960-6f14-4360-95c1-e7a3ba509755" width=50%>

If, for example, you decided to store The TF2 Collection in `C:\Users\example\Documents\TF2 Collection`, here's how your folder structure would look like:
```
C:\Users\example\Documents\TF2 Collection\allclass\allclass.blend
C:\Users\example\Documents\TF2 Collection\allclass2\allclass2.blend
C:\Users\example\Documents\TF2 Collection\allclass3\allclass3.blend
C:\Users\example\Documents\TF2 Collection\scout\scoutcosmetics.blend
C:\Users\example\Documents\TF2 Collection\solder\soldiercosmetics.blend
C:\Users\example\Documents\TF2 Collection\pyro\pyrocosmetics.blend
C:\Users\example\Documents\TF2 Collection\demo\democosmetics.blend
C:\Users\example\Documents\TF2 Collection\heavy\heavycosmetics.blend
C:\Users\example\Documents\TF2 Collection\engineer\engineercosmetics.blend
C:\Users\example\Documents\TF2 Collection\medic\mediccosmetics.blend
C:\Users\example\Documents\TF2 Collection\sniper\snipercosmetics.blend
C:\Users\example\Documents\TF2 Collection\spy\spycosmetics.blend
C:\Users\example\Documents\TF2 Collection\weapons\weapons.blend
```
</details>

Open Blender, and go to `Edit > Preferences > Add-ons > TF2-Trifecta` and click on `Add Paths from Folder.` Select the folder containing all the asset folders and confirm.  
<img src="https://github.com/hisprofile/blenderstuff/assets/41131633/315a4500-3a38-4799-aeed-006d150b5b6f" height=300> <img src="https://github.com/hisprofile/blenderstuff/assets/41131633/25b690f2-85fd-47bd-90d3-3b95e5603fd5" height=300>

Now add a set of rigs.  
