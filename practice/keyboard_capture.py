import PySimpleGUI27 as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

# with sg.Window("Keyboard Test", return_keyboard_events=True, use_default_focus=False) as window:
#     text_elem = sg.Text("", size=(18,1))
#     layout = [[sg.Text("Press a key or scroll mouse")],
#               [text_elem],
#               [sg.Button("OK")]]

#     window.Layout(layout)
#     # ---===--- Loop taking in user input --- #
#     while True:
#         button, value = window.ReadNonBlocking()

#         if button == "OK"  or (button is None and value is None):
#             print(button, "exiting")
#             break
#         if button is not None:
#             print button
#             text_elem.Update(button)

with sg.Window("Realtime Keyboard Test", return_keyboard_events=True, use_default_focus=False) as window:
    layout = [[sg.Text("Hold down a key")],
              [sg.Button("OK")]]

    window.Layout(layout)

    while True:
        button, value = window.ReadNonBlocking()

        if button == "OK":
            print(button, value, "exiting")
            break
        if button is not None:
            print(button)
        elif value is None:
            break