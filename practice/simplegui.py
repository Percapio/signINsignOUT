import PySimpleGUI27 as sg

layout = [  [sg.Text('CPU util')],
            [sg.Text('', size=(8,2), font='Helvetica 20', justification='center', key='_text_')],
            [sg.Exit()]
        ]

window = sg.Window('CPU Percent').Layout(layout)

while True:
    button, values = window.ReadNonBlocking() #What is this executable?

    if button == 'Exit' or values is None:
        break
