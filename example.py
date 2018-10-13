import PySimpleGUI27 as sg
import json
import os
import time

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
            try:
                int(phone_number)
                if int(phone_number) > 9999:
                    sg.Popup('Enter last four of your phone number.')
                elif len(phone_number) < 4:
                    sg.Popup('Enter last four of your phone number.')
                else:
                    failed = fetch_user(phone_number)
                    if failed:
                        sg.Popup('Invalid phone number.')

                    element = window.FindElement('input_box')
                    element.Update('')
            except:
                sg.Popup('Number values only.')
                element = window.FindElement('input_box')
                element.Update('')

def fetch_user(person_number):
    database = os.listdir('./database')

    for grab_file in database:
        location = '{}{}'.format('database/', grab_file)
        data = open(location)
        json_data = json.load(data)

        if int(person_number) == int(json_data['phone'][-4:]):
            json_data = person_info(json_data)

            with open(('./{}'.format(location)), 'w') as outfile:
                json.dump(json_data, outfile)
            return False

        data.close()

    return True

def person_info(json_data):
    layout = [
        [sg.Text(time.asctime(time.localtime(time.time())), font=("Helvetica", 18), justification='center', size=(25,1))],
        [sg.Text('Name: ', size=(10,1), font=("Helvetica", 18)), sg.Text(json_data['name'], font=("Helvetica", 18))],
        [sg.Text('Number: ', size=(10,1), font=("Helvetica", 18)), sg.Text(json_data['phone'], font=("Helvetica", 18))],
        [sg.Text('Is logged in? ', size=(10,1), font=("Helvetica", 18)), sg.Text(str(json_data['signedIN']), font=("Helvetica", 18))],
        [sg.Button('Log In', key='logger'), sg.Button('Cancel')]
    ]

    window = sg.Window('User Information').Layout(layout)

    while True:
        button, values = window.ReadNonBlocking()

        if json_data['signedIN']:
            element = window.FindElement('logger')
            element.Update(text='Log Out')
        
        if button == 'Cancel':
            return json_data
        elif button == 'Log In' or values is None:
            json_data['signedIN'] = True
            json_data['timeLogs'].append(time.asctime(time.localtime(time.time())))
            return json_data
        elif button == 'Log Out' or values is None:
            json_data['signedIN'] = False
            json_data['timeLogs'].append(time.asctime(time.localtime(time.time())))
            return json_data

start_app()