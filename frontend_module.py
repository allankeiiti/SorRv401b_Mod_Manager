"""
    Module that got all functions to load a specific window.

"""

import tkinter as tk


def credits_toplevel():
    """ Test of function that open another window"""
    credits = tk.Toplevel()
    credits_lbl = tk.Label(credits, text='Software Developed By Allan / SpideyKeiiti\n'
                                         'Made for Prototype purposes for Streets Of Rage Remake Community!')

    credits_lbl.pack()
