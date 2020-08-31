"""
    This Script contains all functions used in the project:

    Source: https://stackoverflow.com/questions/55515627/pysimplegui-call-a-function-when-pressing-button
            https://thispointer.com/python-how-to-unzip-a-file-extract-single-multiple-or-all-files-from-a-zip-archive/#:~:text=To%20unzip%20it%20first%20create,()%20on%20that%20object%20i.e.&text=It%20will%20extract%20all%20the%20files%20in%20zip%20at%20current%20Directory.
    check_if_is_sorrv4_folder() - everytime when the program is launched
    check_all_sorr4_files() - everytime when the program is launched
    make_backup() - first time
    check_if_folders_exist() - first time
    create_mods_folders() - first time
    play_music()
"""
import shutil
import subprocess
import os

# Attr
Mods_Cattegories = ['chars', 'enemies']

Chars = ['Axel', 'Blaze', 'Skate', 'Adam', 'Max', 'Zan', 'Shiva', 'MrX']

data = ['logo', '23', '06', 'stage3g', 'item1spa', 'falcon', 'coloredit', 'se34', '29a', 'barbon', 'zan', 'se18',
        'sev12', '28a', '10a', '04a', 'se52', 'sev7', 'sev33', 'stage8b', 'monalisa', 'sev25', 'english', 'se55',
        'sev31', 'se104', 'sev5', 'drdahm', 'sev23', 'finalbossa', 'zamza', 'seskate1', 'stage2b', '13a', '18a',
        'hakuyo', 'stage2f', 'jetx', '26', '25', '00a', 'se105', 'resultado', '27a', 'ninjo', 'stage4c', 'se57',
        'general', 'stage4a', 'robotx', 'se58', 'se39', 'se46', 'se43', 'seaxel4', 'sev39', 'electrax', 'axel',
        'rocket', 'stage6e', 'sev34', 'intro4', 'stage2d', 'se27', 'se11', 'spanish', 'sev40', '19a', '09', '31',
        'se36', 'stage3d', 'cascada', 'sev8', 'jack', 'se4', 'seblaze3', '19', 'cody', 'se19', 'stage7c', 'stage6a',
        'item1eng', 'complete', 'ending3', 'seblaze5', 'se48', 'cargando.png', 'sev27', 'sev42', 'scroll3', 'seg6',
        'seskate5', 'stage5c', 'stage8e', 'intro1', 'se44', '22a', 'stage2g', 'sor1', 'galsia', 'sev22', 'stage3f',
        'stage3i', 'stage8d', 'se9', 'sev37', '21a', 'se29', 'stage5e', 'seg2', '13', 'seg4', '10', '04', 'se22',
        'stage6b', 'se45', 'se37', 'se59', 'se40', 'silver', '09a', '16', 'se54', '18', 'payaso', 'seskate4', 'shivax',
        'se30', 'se41', 'stage3h', 'seg1', '02a', '30a', '00', 'sev13', 'sev36', '20', 'abadede', 'max', '30', 'sev43',
        '23a', 'stage2a', 'yamato', '15', '12', 'sshiva', 'stage3c', 'donovanx', 'se21', 'se3', 'sev24', 'stage5b',
        'sev19', 'semax1', 'letrero', 'sev14', 'ending2', 'semax4', '07', 'barra_amarilla', 'sev44', 'stage5a', 'se20',
        'stage6f', 'rudra', 'se8', 'stage7b', 'se5', 'select1', 'seblaze4', 'sev11', '05', 'loading.png', 'seg7',
        'stage6d', 'se47', 'fgolpe', 'se35', 'semax3', 'p1', 'se38', 'stage6c', 'skate', 'galsia_sor1', '21', 'jet',
        'seg3', 'semax5', 'scroll4', 'se13', 'storm', 'sev17', 'stage7a', 'sev29', 'sev1', 'vice', 'freddy', 'blaze',
        'movie', 'stage2e', 'sev3', 'intro3', '28', 'galsiax', 'sev41', 'camionero', 'se1', 'shiva', 'galeria',
        'cutscenes', '17', 'se10', 'seskate3', 'stage8c', 'finalboss', 'gold', '02', 'se24', 'police', 'se7', 'sev35',
        'polvo', 'se26', 'se103', '14', 'se56', 'seaxel2', 'mrx', 'se17', 'mry', 'stage2c', 'ash', 'ending1', 'sev30',
        'select', 'sev4', 'boomerang', 'stage3a', '16a', 'se6', 'duel', 'sev46', 'ending4', 'sev9', 'se61', 'paletas',
        'se12', 'barra', 'sev10', 'sev26', 'se28', 'sev21', 'seblaze6', '11', 'se33', 'particle', 'se23', 'vball',
        'tiger', 'banderas', '32', 'stage', 'semax2', 'ninjax', 'sev20', 'se2', 'barra_azul', 'seaxel1', 'adam', 'seg8',
        'sev6', 'seskate2', 'neox', 'stage3b', 'rbear', 'vehelits', 'sev28', 'icon', 'sev45', 'electra_sor1', 'sev18',
        'objeto', 'electra', 'sev15', 'seblaze2', 'bongo', '19b', '24', '03', 'seg5', '27', 'galvice', 'stage1e',
        'bronz', 'sorr', 'blaze06', 'superfx', 'item', 'stage1c', 'stage-duel', 'se14', 'intro2', '29', 'sev2', 'roo',
        'stage4b', 'donovan', 'slum', 'se15', 'se53', 'fuente', 'gameover', '31a', 'stage3e', 'se32', 'garnet', 'fuego',
        'credits', 'se51', 'ysignal', 'se60', 'stage1b', 'se31', 'se25', 'se49', 'stage8a', 'sev38', 'bruce', 'stage1a',
        'se50', 'stage5d', '12a', '08', 'se42', 'sev16', 'super_shiva', 'stage1d', 'se16', 'seaxel3', '22', 'sev32',
        'seblaze1']

current_dir = os.getcwd()
project_files = ['sor_module.py']

# SOR Remake V4 files list
sorr4_files = ['data', 'sorr.dat', 'sorr.exe']


def check_if_is_sorrv4_folder():
    """
        This function check if this folder is a SOR Remake V4 Folder, before doing all steps.
        If the current folder contains the data, sorr.dat and sorr.exe file the script is in a SORR V4 Folder.
    :return: True / False
    """
    current_folder_files_list = []
    for file in os.scandir(os.getcwd()):
        current_folder_files_list.append(file.name.lower())

    result = []
    for sorr_file in sorr4_files:
        if sorr_file in current_folder_files_list:
            result.append(True)
        else:
            result.append(False)

    if False not in result:
        return True
    else:
        return False


def check_all_sorr4_files():
    """
        This function checks if all files needed to game run is there, else the program will not run
    :return:
    """
    data_files = []
    for file in os.scandir('data'):
        data_files.append(file.name)

    missing_files = []
    for file in data:
        if file not in data_files:
            missing_files.append(file)

    if len(missing_files) == 0:
        return True
    else:
        return False


def make_backup():
    """
        this function'll be executed once at the start. It'll check if the backup folder exists
        TODO: Remember that not all players doesn't have the vanilla data folder, what about thinking in download
                the files and moving there?
    :return:
    """
    backup_dir = r'Sor_Mods_Storage\backup_folder'
    if ~os.path.exists(backup_dir):
        cmdCommand = fr"mkdir {backup_dir}"  # Copy data dir here
        subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE, shell=True)

    try:
        shutil.copytree('data', backup_dir + r'\data')
        return True
    except FileNotFoundError:
        print('User deleted the backup dir or maybe he do not got permissions on this folder')
        return False
    except PermissionError:
        print('Permission Error')


def check_if_folders_exist():
    """
        Check if the Mods Folder exists in the game root directory
    :return: True / False
    """
    result = []
    result.append(os.path.exists('Sor_Mods_Storage'))

    for folder in Mods_Cattegories:
        result.append(os.path.exists(fr"mkdir Sor_Mods_Storage\{folder}"))

    for folder in Chars:
        result.append(os.path.exists(fr"mkdir Sor_Mods_Storage\chars\{folder}"))

    if False not in result:
        return True
    else:
        return False


def create_mods_folders():
    """
        This function is executed in the first time, like a setup for mods
    :return: None.
    """
    for folder in Mods_Cattegories:
        cmdCommand = fr"mkdir Sor_Mods_Storage\{folder}"  # specify your cmd command
        subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE, shell=True)

    for folder in Chars:
        cmdCommand = fr"mkdir Sor_Mods_Storage\chars\{folder}"  # specify your cmd command
        subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE, shell=True)


def play_music():
    from pygame import mixer
    """ Function used to play music during the tool use, but maybe gonna be scrapped """
    mixer.init()
    mixer.music.load('bg_music.mp3')
    mixer.music.play()


def test_function(mode):
    print(f'Essa Função foi executada! {mode}')


def list_char_mods():
    """
        This function list all Characters Mods inside Sor_Mods_Storage\chars folder, and will be executed during the
        Char Mods window rendering.
        Is recommended to put the folder with the Mod Files, but I programmed it to find out if the folder is empty or
        have game files in it.
        If you put a compressed file, it'll uncompress!
    :return: List of mods
    """
    list_chars = []  # Will store a Final char list as output from the function
    char_mods_dirs = []  # Will store the char folders with respective files
    files_to_uncompress = []  # Will store the files that are compressed
    chars_dir = r'Sor_Mods_Storage\chars'

    # 1 - Scanning the chars mod Folder
    for mods in os.scandir(chars_dir):
        if os.path.isdir(chars_dir + '\\' + mods.name):
            char_mods_dirs.append(mods.name)
        else:
            for compressed_suffix in ['.zip', '.rar', '.7z', '.001']:
                if mods.name.__contains__(compressed_suffix):
                    files_to_uncompress.append(mods.name)

    # 2 - Making the adjustments in the char_dirs_mods, looking if they are folders with real mod files
    # (If contains 1 file at least, will be added to list_chars)
    for char_mods_dir in char_mods_dirs:
        for file in os.scandir(chars_dir + '\\' + char_mods_dir):
            if file.name in data:
                list_chars.append(char_mods_dir.name)

    return list_chars
