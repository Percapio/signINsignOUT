**signINsignOUT**

A simple step-by-step guide to building a Log In/Out application using Python 2.7.

<br />

**Table of Contents**
- [Introduction](#introduction)
    - [Summary](#summary)
    - [Setup](#setup)
- [Start App](#start-app)
    - [Initial Setup 1](#initial-setup-1)
    - [Create the Window](#create-the-window)
- [User Data](#user-data)
    - [Prepping the Data](#prepping-the-data)
- [Fetch User](#fetch-user)
    - [Initial Setup 2](#initial-setup-2)
    - [Check for User](#check-for-user)
- [User Info](#user-info)
    - [Initial Setup 3](#initial-setup-3)
    - [Display Information](#display-information)
    - [Test the Program 1](#test-the-program-1)
- [Complete the Program](#complete-the-program)
    - [Proper Input Sanitizing](#proper-input-sanitizing)
    - [Test the Program 2](#test-the-program-2)
    - [Complete Start App](#complete-start-app)
    - [Complete Fetch User](#complete-fetch-user)
    - [Complete User Info](#complete-user-info)
- [Technology Used](#technology-used)
- [Resources](#resources)

<br />

## Introduction
### Summary

&nbsp;&nbsp;&nbsp;&nbsp; This guide is designed to be instructions on how to build a small log in and out program.  The program will ask users for an input, and will check if the input is four digits.  If it is, then it will compare the input value to people currently saved in the database.  If this particular check is true, then it will display another screen to ask the users if they wish to log in or out.  If any of the previous checks are not true then the users will receive the proper errors to inform them of what went wrong during the process.

&nbsp;&nbsp;&nbsp;&nbsp; You are expected to have a basic understanding of Terminal Bash and programming.  It would help if you knew Python, but it is not required.  Additionally, this guide will be assuming the program is written in a MacOSX environment, but the steps in the Startup section can be easily replaced with whichever OS you are most comfortable with.

### Setup

To begin, let's make sure Python 2.7 is on your computer.
```
$ python --version
```
![alt text](./images/python_version.png 'Python Version 2.7.15')

If it's not present, or the version is incorrect, please refer to the proper documentation for installing/updatng Python:

- [MacOSX](https://www.python.org/downloads/)

Next, you will be using Python package called PySimpleGUI27 for your project, so you will need to install it.
```
$ pip install pysimplegui
```

<br />

## Start App
### Initial Setup 1

After creating a file (such as [example.py](./example.py)), import the PySimpleGUI27 package.
```
import PySimpleGUI27 as sg
```

Create the function to the first part of your program.
```
def start_app():
```

Then setup what you want your application to display.  In this case, it is going to be some text, an input box, and a few buttons.
```
def start_app():
    layout = [
        [sg.Text('Enter the last four of your phone number', size=(75, 1), justification='center', font=("Helvetica", 18))],
        [sg.InputText(font=("Helvetica", 18), justification='center', size=(25,1), key='input_box')],
        [sg.ReadButton('Submit'), sg.ReadButton('Clear')],
        [sg.Exit(key='Exit')]
    ]
```

### Create the Window

Set the window variable to start PySimpleGUI27 and be sure to include all of your layout configurations.
```
window = sg.Window('Log In/Out', auto_size_buttons=False, return_keyboard_events=True).Layout(layout)
```

As a heads up, the *return_keyboard_events* parameter allows keyboard inputs to be saved for future use.

In the next part, you want to make sure the application stays open, so write a *while* loop with a *break* command to allow users a way to exit the program.
```
while True:
    button, values = window.Read()

    if button == 'Exit' or values is None:
        break
```

Test the function and see the beginnings of your hard work.  Don't forget to make sure to call the function at the end of your python file.

![alt text](./images/screen1.png 'Input box and buttons')

In the next part, you are going to create some fake data to test your program.  Onwards!

<br />

## User Data
### Prepping the Data

You need some data to test your application.  If you don't want to build it yourself, there is always [JSON-generator](https://www.json-generator.com/).
```
{
    "name": "Winters Cunningham",
    "email": "winterscunningham@coash.com",
    "phone": "+1 (944) 451-3426",
    "signedIN": true,
}
```

Create a folder called *database* in your project folder to keep your files organized and easily retrievable.
```
$ mkdir database
```

The next few sections will cover the creation of a few new functions as well as returning to the previously made function for updating.

<br />

## Fetch User
### Initial Setup 2

Before starting your Fetch User function, import the necessary packages.
```
import json
import os
```

Then create the function and set your fake data to be retrieved with the given phone number.
```
def fetch_user(phone_number):
    database = os.listdir('./database')
```

### Check for User

Create a *for* loop to step through the database.
```
for grab_file in database:
    location = '{}{}'.format('database/', grab_file)
    data = open(location)
    json_data = json.load(data)
```

Within the *for* loop, check if the current JSON file is going to contain the phone number you are looking for.  If it does then run a function called *user_info* (you are going to write this function this later).
```
if int(phone_number) == int(json_data['phone'][-4:]):
    user_info(json_data)
    break
```

Before you move onto the next function, don't forget that it is best practice to close the file at the end of every iteration.

<br />

## User Info
### Initial Setup 3

The purpose of this function is to check if a user exists in a database, and if he is then to open a second display window with all the necessary information.

In the modal (secondary display window), you want some time to be displayed, so *import time* and write your function header.
```
import time

def user_info(json_data):
```

Much like the *start_app* function you made earier, create a layout with all the necessary data and initialize the window variable.
```
layout = [
    [sg.Text(time.asctime(time.localtime(time.time())), font=("Helvetica", 18), justification='center', size=(25,1))],
    [sg.Text('Name: ', size=(10,1), font=("Helvetica", 18)), sg.Text(json_data['name'], font=("Helvetica", 18))],
    [sg.Text('Number: ', size=(10,1), font=("Helvetica", 18)), sg.Text(json_data['phone'], font=("Helvetica", 18))],
    [sg.Text('Is logged in? ', size=(10,1), font=("Helvetica", 18)), sg.Text(str(json_data['signedIN']), font=("Helvetica", 18))],
    [sg.Button('Log In', key='logger'), sg.Button('Cancel')]
]

window = sg.Window('User Information').Layout(layout)
```

### Display Information

Create a *while* loop with all the conditional statements necessary to *break* out of the loop.  For testing cases, make every possible condition close the window.
```
while True:
    button, values = window.ReadNonBlocking()

    if button == 'Cancel':
        break
    elif button == 'Log In' or values is None:
        break
    elif button == 'Log Out' or values is None:
        break
```

### Test the Program 1

To test the program, update your *start_app* function to add an additonal button check and run the *fetch_user* function.
```
elif button == 'Submit':
fetch_user(phone_number)
```

Now, time to test the program.

![alt text](./images/screen2.png 'A Wild Modal has Appeared')

Awesome!  Looks like everythig works!  Almost done. Onwards!

<br />

## Complete the Program
### Proper Input Sanitizing

While you are in the *start_app* function, add a few steps to implement some basic sanitization on the input.  You don't want someone to accidently inject a script into your program and cause some unintended effects.

First, add *try and except* statements inside the *Submit* check. Then write the clauses to check if the input is number values and to notify the users when the input is not.
```
elif button == 'Submit':
    phone_number = values['input_box']

    try:
        int(phone_number)
        fetch_user(phone_number)
    except:
        sg.Popup('Number values only.')
        element = window.FindElement('input_box')
        element.Update('')
```

The lines with the variable *element* in it are for clearing the input box of all written text.

Within the *try* clause, add an additional conditional statement to check if the number value is within the range you are checking for.
```
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
```

### Test the Program 2

Time for some more integration testing.  Run and test the program.
![alt text](./images/screen4.png 'Test of Too Little Input Numbers')
![alt text](./images/screen3.png 'Test of Too Many Input Numbers')

Looks great!

### Complete Start App

While you are here, finish the *start_app* function by adding a *Clear* button check to clear the input screen, and *enter* key check on the *Submit* conditional statement.
```
elif button == 'Clear':
    element = window.FindElement('input_box')
    element.Update('')
elif button == 'Submit' or ord(str(button)) == 13:
```

To reduce the chances of errors, you want to check for the *Clear* button first before the *Submit* button.

### Complete Fetch User

Update this function to change the user's new log in/out data and time stamps.
```
json_data = user_info(json_data)

with open(('./{}'.format(location)), 'w') as outfile:
    json.dump(json_data, outfile)
return False
```

The *return False* statement is used to determine whether or not there to inform the user the phone number provided is not in the database.  Make sure to add a corresponding *True* statement outside of the *for* loop.

### Complete User Info

Add a check for whether or not the user is logged in and display the correct 'Log In' or 'Log Out' button.
```
if json_data['signedIN']:
    element = window.FindElement('logger')
    element.Update(text='Log Out')
```

Update the conditional statements to modify the relevant data of the user.
```
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
```

Program complete!  Well done!

<br />

## Technology Used
- Technology
    - [Python 2.7](https://docs.python.org/2/)
- Package Downloaded
    - [PySimpleGUI27](https://pypi.org/project/PySimpleGUI27/)
- Default Python 2.7 Packages Used
    - [JSON](https://docs.python.org/2/library/json.html)
    - [OS](https://docs.python.org/2/library/os.html)
    - [Time](https://docs.python.org/2/library/os.html)

<br />

## Resources
- [PySimpleGUI27 Documentation](https://pysimplegui.readthedocs.io/)