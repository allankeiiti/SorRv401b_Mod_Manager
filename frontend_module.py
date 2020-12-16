"""
    Module that got all functions to load a specific window.

"""

import tkinter as tk
from tkinter import ttk
import sor_module
from PIL import ImageTk, Image


def credits_toplevel():
    """ Test of function that open another window"""
    credits = tk.Toplevel()
    credits_lbl = tk.Label(credits, text='Software Developed By Allan / SpideyKeiiti\n'
                                         'Made for Prototype purposes for Streets Of Rage Remake Community!')

    credits_lbl.pack()


def chars_window():
    """
        Function that represents the window where Character Mods can be applied.
    :return:
    """
    char_mods_dict = sor_module.list_char_mods()

    # Loading Images to screen
    chars = tk.Toplevel()
    mainTitleImg = ImageTk.PhotoImage(Image.open(r'img/Photo_PlaceHolder_Axel_By_Daniel2221.png'))
    imgRandom_label = tk.Label(chars, image=mainTitleImg)
    title = tk.Label(chars, text="Characters Mods.")

    comboBox_chars = ttk.Combobox(chars, values=list(char_mods_dict.keys()))

    def print_char_test():
        char_selected = comboBox_chars.get()
        result_window = tk.Toplevel()

        value = ''
        if char_selected == '':
            value = f'{value} Please Select an Mod to Apply!'
        else:
            sor_module.apply_mod(f'Sor_Mods_Storage\chars', mod=char_selected, type='chars')
            value = f'Character Mod {char_selected} applied! Have fun!'

        result_label = tk.Label(result_window, text=value)
        result_label.pack()

    btn_apply = tk.Button(chars, text='Apply', command=print_char_test)

    title.grid(row=0, column=0)
    comboBox_chars.grid(row=1, column=0)
    imgRandom_label.grid(row=1, column=1)
    btn_apply.grid(row=2, column=0)
