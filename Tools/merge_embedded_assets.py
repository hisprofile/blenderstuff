from glob import glob
import os
import shutil
import sys

# Game Folder
# Set this variable to the game folder that "models" and "materials" will be under!
game = r'H:\Games\steamapps\common\Team Fortress 2\tf'

if not (os.path.exists(os.path.join(game, 'models')) and os.path.exists(os.path.join(game, 'materials'))):
    print('Error: "models" or "materials" folder cannot be found!')
    sys.exit()

# .VMF Folder Directory
root_dir = r'C:\maps'

def move_files(file_list):
    for file in file_list:
        file_name = os.path.basename(file)
        folder = file.replace('\\', '/')
        folder = '/'.join(folder.split('/')[1:-1])

        game_folder = os.path.join(game, folder)
        if not os.path.exists(game_folder):
            os.makedirs(game_folder)

        src_path = os.path.join(root_dir, file)
        dst_path = os.path.join(game_folder, file_name)

        if not os.path.exists(dst_path):
            shutil.move(src_path, dst_path)
            print(f'MOVED: {src_path} -> {dst_path}')
        else:
            print(f'SKIPPING (already exists): {file}')

# Finding and moving model and material files
mdls = glob('*_d/models/**/*.*', root_dir=root_dir, recursive=True)
vmts = glob('*_d/materials/**/*.*', root_dir=root_dir, recursive=True)

move_files(mdls)
move_files(vmts)

print('File moving completed.')
