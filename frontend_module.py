"""
    Module that got all functions to load a specific window.

"""

import tkinter as tk
from tkinter import ttk
import sor_module
from PIL import ImageTk, Image


def credits_window():
    """ Test of function that open another window"""
    credits = tk.Toplevel()
    credits_lbl = tk.Label(credits, text='Software Developed By Allan / SpideyKeiiti\n'
                                         'Made for Prototype purposes for Streets Of Rage Remake Community!')

    credits_lbl.pack()


def chars_window():
    """
        Function that represents the window which Character Mods can be applied.
    :return:
    """
    char_mods_dict = sor_module.list_char_mods()

    # Loading Images to screen
    chars = tk.Toplevel()
    mainTitleImg = ImageTk.PhotoImage(Image.open(r'img/Photo_PlaceHolder_Axel_By_Daniel2221.png'))
    imgRandom_label = tk.Label(chars, image=mainTitleImg)
    title = tk.Label(chars, text="Characters Mods")

    comboBox_chars = ttk.Combobox(chars, values=list(char_mods_dict.keys()))

    def apply_char_mod():
        char_selected = comboBox_chars.get()
        result_window = tk.Toplevel()

        value = ''
        if char_selected == '':
            value = f'{value} Please Select an Mod to Apply!'
        else:
            sor_module.apply_mod(f'Sor_Mods_Storage\chars', mod=char_selected, type='chars')
            value = f'Character Mod {char_selected} applied!'

        result_label = tk.Label(result_window, text=value)
        result_label.pack()

    btn_apply = tk.Button(chars, text='Apply', command=apply_char_mod)

    title.grid(row=0, column=0)
    comboBox_chars.grid(row=1, column=0)
    imgRandom_label.grid(row=1, column=1)
    btn_apply.grid(row=2, column=0)


def enemy_window():
    """
        Function that represents the window which Enemy Mods can be applied.
    :return:
    """
    enemy_mods_dict = sor_module.list_char_mods(path_dir=r'Sor_Mods_Storage\enemies')

    # Loading Images to screen
    enemies = tk.Toplevel()
    mainTitleImg = ImageTk.PhotoImage(Image.open(r'img/Photo_PlaceHolder_Axel_By_Daniel2221.png'))
    imgRandom_label = tk.Label(enemies, image=mainTitleImg)
    title = tk.Label(enemies, text="Enemies Mods")

    comboBox_enemies = ttk.Combobox(enemies, values=list(enemy_mods_dict.keys()))

    def apply_enemy_mod():
        char_selected = comboBox_enemies.get()
        result_window = tk.Toplevel()

        value = ''
        if char_selected == '':
            value = f'{value} Please Select an Mod to Apply!'
        else:
            sor_module.apply_mod(f'Sor_Mods_Storage\enemies', mod=char_selected, type='chars')
            value = f'Enemy Mod {char_selected} applied!'

        result_label = tk.Label(result_window, text=value)
        result_label.pack()

    btn_apply = tk.Button(enemies, text='Apply', command=apply_enemy_mod)

    title.grid(row=0, column=0)
    comboBox_enemies.grid(row=1, column=0)
    imgRandom_label.grid(row=1, column=1)
    btn_apply.grid(row=2, column=0)


def pallete_window():
    """
        Function that represents the window which Enemy Mods can be applied.
    :return:
    """
    char_mods_dict = sor_module.list_char_mods(path_dir=r'Sor_Mods_Storage\palletes')

    # Loading Images to screen
    palletes = tk.Toplevel()
    mainTitleImg = ImageTk.PhotoImage(Image.open(r'img/Photo_PlaceHolder_Axel_By_Daniel2221.png'))
    imgRandom_label = tk.Label(palletes, image=mainTitleImg)
    title = tk.Label(palletes, text="Pallete Mods")

    comboBox_palletes = ttk.Combobox(palletes, values=list(char_mods_dict.keys()))

    def apply_pallete_mod():
        pallete_selected = comboBox_palletes.get()
        result_window = tk.Toplevel()

        value = ''
        if pallete_selected == '':
            value = f'{value} Please Select an Pallete to Apply!'
        else:
            sor_module.apply_mod(f'Sor_Mods_Storage\enemies', mod=pallete_selected, type='chars')
            value = f'Enemy Mod {pallete_selected} applied!'

        result_label = tk.Label(result_window, text=value)
        result_label.pack()

    btn_apply = tk.Button(palletes, text='Apply', command=apply_pallete_mod)

    title.grid(row=0, column=0)
    comboBox_palletes.grid(row=1, column=0)
    imgRandom_label.grid(row=1, column=1)
    btn_apply.grid(row=2, column=0)


def stage_window():
    """
        Function that represents the window which Stage Mods can be applied.
    :return:
    """
    stage_mods_dict = sor_module.list_char_mods(path_dir=r'Sor_Mods_Storage\stages')

    # Loading Images to screen
    stages = tk.Toplevel()
    mainTitleImg = ImageTk.PhotoImage(Image.open(r'img/Photo_PlaceHolder_Axel_By_Daniel2221.png'))
    imgRandom_label = tk.Label(stages, image=mainTitleImg)
    title = tk.Label(stages, text="Stage Mods")

    comboBox_chars = ttk.Combobox(stages, values=list(stage_mods_dict.keys()))

    def apply_stage_mod():
        stage_selected = comboBox_chars.get()
        result_window = tk.Toplevel()

        value = ''
        if stage_selected == '':
            value = f'{value} Please Select an Stage Mod to Apply!'
        else:
            sor_module.apply_mod(f'Sor_Mods_Storage\stages', mod=stage_selected, type='chars')
            value = f'Enemy Mod {stage_selected} applied!'

        result_label = tk.Label(result_window, text=value)
        result_label.pack()

    btn_apply = tk.Button(stages, text='Apply', command=apply_stage_mod)

    title.grid(row=0, column=0)
    comboBox_chars.grid(row=1, column=0)
    imgRandom_label.grid(row=1, column=1)
    btn_apply.grid(row=2, column=0)
