import PySimpleGUI27 as sg
import json
import os
import time


def person_info(name, number, logged_in, time_logs):
    layout = [
        [sg.Text(' ', size=(75, 2))],
        [sg.Text(' ', size=(15, 1)), sg.Text(time.asctime(time.localtime(time.time())), font=("Helvetica", 18), justification='center', size=(25,1))],
        [sg.Text(' ', size=(15, 1)), sg.Text('Name: ', size=(10,1), font=("Helvetica", 18)), sg.Text(name, font=("Helvetica", 18))],
        [sg.Text(' ', size=(15, 1)), sg.Text('Number: ', size=(10,1), font=("Helvetica", 18)), sg.Text(number, font=("Helvetica", 18))],
        [sg.Text(' ', size=(15, 1)), sg.Text('Is logged in? ', size=(10,1), font=("Helvetica", 18)), sg.Text(str(logged_in), font=("Helvetica", 18))],
        [sg.Text(' ', size=(15, 2))],
        [sg.Text(' ', size=(20, 3)), sg.Button('Log In', key='logger'), sg.Button('Cancel')]
    ]

    window = sg.Window('User Information').Layout(layout)

    while True:
        button, values = window.ReadNonBlocking()

        if logged_in:
            element = window.FindElement('logger')
            element.Update(text='Log Out')
        
        if button == 'Cancel':
            break
        elif button == 'Log In' or values is None:
            break
        elif button == 'Log Out' or values is None:
            break

def check_data(dataJSON, person_number):
    last_four = int(dataJSON['phone'][-4:])
    return last_four == int(person_number)

def fetch_person(person_number):
    directory = os.listdir('/Users/npowerair28/Documents/PythonProject/database')
    num_files = len(directory)
    counter = 0

    for grab_file in directory:
        location = '{}{}'.format('database/', grab_file)
        data = open(location)
        dataJSON = json.load(data)

        if check_data(dataJSON, person_number):
            name = dataJSON['name']
            number = dataJSON['phone']
            logged_in = dataJSON['signedIN']
            time_logs = dataJSON['timeLogs']

            person_info(name, number, logged_in, time_logs)
            break
        else:
            counter += 1

        data.close()
    
    if counter == num_files:
        sg.Popup('Invalid Number.')

def num_logged_in():
    directory = os.listdir('./database')
    num_files = len(directory)
    counter = 0

    for grab_file in directory:
        location = '{}{}'.format('database/', grab_file)
        data = open(location)
        dataJSON = json.load(data)

        if dataJSON['signedIN']:
            counter += 1

    return str(counter)

def start_app():
    layout = [
        [sg.Text(' ', size=(75, 2))],
        [sg.Text('Enter the last four of your phone number', size=(75, 1), justification='center', font=("Helvetica", 18))],
        [sg.Text(' ', size=(37,1)), sg.InputText(font=("Helvetica", 18), justification='center', size=(25,1))],
        [sg.Text(' ', size=(35,1)), sg.ReadButton('Submit'), sg.Text(' ', size=(15,1)), sg.ReadButton('Clear')],
        [sg.Text(' ', size=(75,2))],
        [sg.Exit(button_color=('white', 'red'), key='Exit'), sg.Text(' ', size=(90,1)), 
            sg.Text('Number logged in:       {}'.format(num_logged_in()), font=("Helvetica", 12))]
    ]

    window = sg.Window('NPower Log In/Out', auto_size_buttons=False, return_keyboard_events=True).Layout(layout)

    keys_entered = ''
    while True:
        button, (user_input) = window.Read()

        if button == 'Exit' or user_input is None:
            break
        elif button == 'Clear':
            user_input[0] = ''
        elif button == 'Submit' or (ord(str(button))) == 13:
            try:
                int(user_input[0])
                if int(user_input[0]) > 9999:
                    sg.Popup('Enter last four of your phone number.')
                elif len(user_input[0]) < 4:
                    sg.Popup('Enter last four of your phone number.')
                else:
                    fetch_person(user_input[0])
            except:
                sg.Popup('Number values only.')
                user_input[0] = ''

start_app()