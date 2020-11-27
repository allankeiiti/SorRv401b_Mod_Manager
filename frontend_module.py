"""
    Module that got all functions to load a specific window.

"""

import tkinter as tk
from tkinter import ttk
import sor_module


def credits_toplevel():
    """ Test of function that open another window"""
    credits = tk.Toplevel()
    credits_lbl = tk.Label(credits, text='Software Developed By Allan / SpideyKeiiti\n'
                                         'Made for Prototype purposes for Streets Of Rage Remake Community!')

    credits_lbl.pack()


def chars_window():
    char_mods_dict = sor_module.list_char_mods()

    chars = tk.Toplevel()
    comboBox_chars = ttk.Combobox(chars, values=list(char_mods_dict.keys()))

    comboBox_chars.pack()
