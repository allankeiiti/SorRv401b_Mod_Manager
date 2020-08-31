import PySimpleGUI as sg

width, height = 68, 150
title = 'Allan\'s Python Project - v4.01b Mod Manager'

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

sg.Window(title, layout=[[]], margins=(width, height)).read()
