"""
    === ROOT ===
    Sources

    TkInter Tutorial:
    https://www.youtube.com/watch?v=YXPyB4XeYLA&t=1532s

    Music Icon:
    https://www.flaticon.com/free-icon/musical-note_727204?term=music&page=1&position=18
"""

import tkinter as tk
import sor_module
import frontend_module
from PIL import ImageTk, Image


# Initializing the Root screen
root = tk.Tk()
root.iconbitmap(r'img/link_icon.ico')
root.title('Allan\'s SorR 4.01 Mod Manager')

# Loading Images to screen
mainTitleImg = ImageTk.PhotoImage(Image.open(r'img/041.png'))
imgTitle_label = tk.Label(image=mainTitleImg)

musicImg = ImageTk.PhotoImage(Image.open(r'img/musical-note.png'))


title = tk.Label(root, text="SOR Remake V4.01 \n Mod Manager")
music_btn = tk.Button(root, command=sor_module.play_music, image=musicImg)


# Mod Menu Buttons
menu_frame = tk.LabelFrame(root, text='Mod Options', padx=10, pady=10)
char_btn = tk.Button(menu_frame, text='Char Mods', command=frontend_module.chars_window)
enemy_btn = tk.Button(menu_frame, text='Enemy Mods')
palette_btn = tk.Button(menu_frame, text='Palettes')
stage_btn = tk.Button(menu_frame, text='Stage Mods')
credits_btn = tk.Button(menu_frame, text='Credits', command=frontend_module.credits_toplevel)

# Exit
exit_btn = tk.Button(root, text='Exit', command=root.quit)


# Layout Inicial - 5 colunas
music_btn.grid(row=0, column=0)
title.grid(row=0, column=3)


# Appearance Layout
imgTitle_label.grid(row=1, column=1, columnspan=2)


# Buttons Layout
menu_frame.grid(row=4, column=1)
char_btn.grid(row=3, column=0)
enemy_btn.grid(row=3, column=1)
palette_btn.grid(row=3, column=2)
stage_btn.grid(row=3, column=3)
credits_btn.grid(row=3, column=4)
exit_btn.grid(row=4, column=3)

root.mainloop()
