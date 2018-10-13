import PySimpleGUI27 as sg

def start_app():
    layout = [
        [sg.Text('Enter the last four of your phone number', size=(75, 1), justification='center', font=("Helvetica", 18))],
        [sg.InputText(font=("Helvetica", 18), justification='center', size=(25,1), key='input_box')],
        [sg.ReadButton('Submit'), sg.ReadButton('Clear')],
        [sg.Exit(key='Exit')]
    ]

    window = sg.Window('Log In/Out', auto_size_buttons=False, return_keyboard_events=True).Layout(layout)

    while True:
        button, values = window.Read()

        if button == 'Exit' or values is None:
            break
        elif button == 'Clear':
            element = window.FindElement('input_box')
            element.Update('')
        elif button == 'Submit' or ord(str(button)) == 13:
            phone_number = values['input_box']
            
            # try:
            #     int(phone_number)
            #     if int(phone_number) > 9999:
            #         sg.Popup('Enter last four of your phone number.')
            #     elif len(phone_number) < 4:
            #         sg.Popup('Enter last four of your phone number.')
            #     else:
                    # failed = fetch_person(phone_number)
            #         if failed:
            #             sg.Popup('Invalid phone number.')

            #         element = window.FindElement('input_box')
            #         element.Update('')
            # except:
            #     sg.Popup('Number values only.')
            #     element = window.FindElement('input_box')
            #     element.Update('')
