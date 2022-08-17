def print_operations():
    """
    Runs all the print and string operations, consisting basic python scenarios
    """
    # Simple print statement
    print("Hitesh")
    # formatted print
    name = 'Hitesh'
    surname = 'Pandey'
    print(f"My name is {name} {surname}")

    # Operator * operation on string to numerical
    # Python doesn't give error in this case
    # It will instead print * ten times
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
