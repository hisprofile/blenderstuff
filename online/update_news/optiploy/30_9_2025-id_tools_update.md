# OptiPloy "ID Tools" Update
## General
- Code refactoring
- Moved properties to WinMan
- You are now able to move OptiPloy into another category within the viewport
- Fixed a major flaw involving the import of sub-collections

## Drag 'n' Drop (Pro Only)
- Fixed a bug that would prevent rotation from being added onto the rig
- Added a "Constant Pad Scale" feature (toggle with A)

## ID Tools
A set of ID tools has been added to OptiPloy to allow more flexibility over what gets imported, and how it gets imported
Tools are available in the Outliner or Properties Context Menu
- ID Attach / Quick Attach
  - Quickly attaches an ID to a Host ID, always ensuring the import of the parasitic ID(s)
- Remove Selected ID(s) from Host(s)
  - Ensures the selected parasitic IDs do NOT get imported
- Removed ID(s) from Selected Hosts(s)
  - Removes any possibly attached parasitic IDs from the selected Host IDs
- Make Properties Overridable
  - Enables all custom properties on the ID to be library overridden
- User Path Report (Pro Only)
  - Prints a report of where an ID is used and the path that leads to it.

## ID Behavior
You can now set how IDs are treated in the import process. The three options are:
- Do Nothing
- Prefer Override
  - Prefer ID being overridden over being localized
- Stay Linked
  - Ensure the ID stays linked

# Photos
###### New ID Tools  
<img width="730" height="295" alt="image" src="https://github.com/user-attachments/assets/e77666db-16f1-4073-b0c3-9832079cd874" />
<img width="606" height="282" alt="image" src="https://github.com/user-attachments/assets/1d43da3f-001f-43b7-a08d-eece833cce5e" />  

###### User Path Report Feature (Pro Only)  
<img width="551" height="434" alt="image" src="https://github.com/user-attachments/assets/edd6eb4f-afde-43e2-8231-570a3b130c46" />  

###### Custom Panel Placement
<img width="894" height="645" alt="image" src="https://github.com/user-attachments/assets/3fca01ee-f510-4d92-911d-8d7df8af4ad9" />

