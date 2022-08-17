def print_operations():
    """
    Runs all of the print and string operations, consisting basic python scenarios
    """
    # simple print statement
    print("Hitesh")
    # formatted print
    name = 'Hitesh'
    surname = 'Pandey'
    print(f"My name is {name} {surname}")

    # operator * operation on string to numerical
    # python doesn't give error in this case
    # it will instead print * ten times
    print('*' * 10)


def get_user_input():
    """
    Really basic method to get user input from terminal
    """
    # This is really useful for creating a command line program
    name = input('Enter nane')
    print(f'Hi {name}')
    color = input('Enter your favorite color')
    print(f'{name} like {color}')
