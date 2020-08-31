import PySimpleGUI as sg
import pygame
from sor_module import test_function

# Very basic form.  Return values as a list
# https://opensource.com/article/18/8/pysimplegui

title = 'Allan\'s Project - SorR 4.01b Mod Manager'
form = sg.Window(title)  # begin with a blank form

layout = [
          [sg.SimpleButton('Play Music'), sg.Text('\n\n\n\n\n')],
          [sg.Text('Char Mods', size=(15, 1)), sg.InputText('name')],
          [sg.Text('E', size=(15, 1)), sg.InputText('address')],
          [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
          # [sg.Image(data=r'img\figure1.png')],
          [sg.SimpleButton('Char \nMods'), sg.SimpleButton('Enemy \nMods'), sg.SimpleButton('Stage \nMods'),
           sg.SimpleButton('Palettes'), sg.SimpleButton('Credits')]
         ]

button, values = form.Layout(layout).read()

print('Char' in button)
print(button)
if 'Char' in button:

    char_form = sg.Window(title + ' - Char Mods')

    char_layout = [[sg.Text('Character Mods Manager')],
                   [sg.Listbox(values=['Vai', 'Vai', 'Será que foi'], size=(30, 3))],
                   [sg.SimpleButton('Set')]
                   ]

    resp = char_form.Layout(char_layout).read()
    print(resp)
    if 'Set' in str(resp):
        test_function('Mods Medu')
    char_form.close()

print(button, values)
form.close()
