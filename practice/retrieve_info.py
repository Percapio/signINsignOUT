import os
import json

def check_data(_dataJSON, person_number):
    _last_four = int(_dataJSON['phone'][-4:])
    return _last_four == person_number

def fetch_person(person_number):
    for _file in os.listdir('/Users/npowerair28/Documents/PythonProject/database'):
        _location = '{}{}'.format('database/',_file)
        _data = open(_location)
        _dataJSON = json.load(_data)

        if check_data(_dataJSON,person_number):
            _name = _dataJSON['name']
            _number = _dataJSON['phone']
            _logged_in = _dataJSON['signedIN']
            _time_logs = _dataJSON['timeLogs']

            print ('\n{}  :  {}'.format(_name,_number))
            print ('Is logged in? {}\n'.format(_logged_in))

        _data.close()

def request_input():
    print ('Enter "esc" at anytime to exit.')

    while True:
        try:
            _data = raw_input('Please, enter last four of your phone number: ')
            if _data.lower() == 'esc':
                break
            elif int(_data):
                if int(_data) > 9999:
                    print ('Enter four numbers.')
                else:
                    return fetch_person(int(_data))
        except:
            print ('Enter four numbers')

request_input()
