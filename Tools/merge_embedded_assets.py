from glob import glob
import os, shutil, sys

# Game Folder
# Set this variable to the game folder that "models" and "materials" will be under!
game = r'H:\Games\steamapps\common\Team Fortress 2\tf'

try:
    assert os.path.exists(os.path.join(game, 'models'))
    assert os.path.exists(os.path.join(game, 'materials'))
except AssertionError:
    input('models or materials folder cannot be found! Press Enter to stop!')
    sys.exit()

# .VMF Folder Directory
root_dir =r'C:\maps'


models = glob('*_d/models/', root_dir=root_dir)
materials = glob('*_d/materials/', root_dir=root_dir)
vmts = glob('*_d/materials/**/*.*', root_dir=root_dir, recursive=True)
mdls = glob('*_d/models/**/*.*', root_dir=root_dir, recursive=True)

for mdl in mdls:
    mdl_name = os.path.basename(mdl)
    folder = mdl.replace('\\', '/')
    folder = '/'.join(folder.split('/')[1:-1])

    game_folder = os.path.join(game, folder)
    if not os.path.exists(game_folder):
        os.makedirs(game_folder)

    if not os.path.exists(os.path.join(game_folder, mdl_name)):
        shutil.move(os.path.join(root_dir, mdl), os.path.join(game_folder, mdl_name))
    else:
        print(f'SKIPPING {mdl}')

    #input((os.path.join(root_dir, mdl), os.path.join(game_folder, mdl_name)))

for vmt in vmts:
    vmt_name = os.path.basename(vmt)
    folder = vmt.replace('\\', '/')
    folder = '/'.join(folder.split('/')[1:-1])

    game_folder = os.path.join(game, folder)
    if not os.path.exists(game_folder):
        os.makedirs(game_folder)

    if not os.path.exists(os.path.join(game_folder, vmt_name)):
        shutil.move(os.path.join(root_dir, vmt), os.path.join(game_folder, vmt_name))
    
    else:
        print(f'SKIPPING {vmt}')
