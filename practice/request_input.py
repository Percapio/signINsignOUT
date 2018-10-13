def request_input():
    print ('Enter "esc" at anytime to exit.')

    while True:
        try:
            _data = raw_input('Please, enter last four of your phone number: ')
            if _data.lower() == 'esc':
                break
            elif int(_data):
                if int(_data) > 9999:
                    print ('Enter only four numbers, please')
                elif int(_data) < 1000:
                    print ('{}{}'.format('0',_data))
                else:
                    print (_data)
        except:
            print ('Enter only four numbers')

request_input()

