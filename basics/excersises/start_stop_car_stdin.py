def run():
    carstatus = ''
    while (True):
        val = input("Enter a car function: 'Start', 'Stop', 'Quit': ")
        if val.lower() == 'start':
            if carstatus == 'start':
                print('Car is already Running')
            else:
                print('Car Started')
                carstatus = 'start'
        elif val.lower() == 'stop':
            if carstatus == 'stop':
                print('Car is already Stopped')
            else:
                print('Car Stopped')
                carstatus = 'stop'
        elif val.lower() == 'quit':
            print('bye')
            break
        else:
            print("Invaild arguement")

run()