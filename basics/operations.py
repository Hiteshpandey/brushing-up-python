# For math operations
import math


def print_operations():
    """
    Runs all the print and string operations, consisting basic python scenarios
    """
    """
        Format: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
        objects - object to the printed. * indicates that there may be more than one object
        sep - objects are separated by sep. Default value: ' '
        end - end is printed at last
        file - must be an object with write(string) method. If omitted, sys.stdout will be used which prints objects on the screen.
        flush - If True, the stream is forcibly flushed. Default value: False
    """
    # Simple print statement
    print("Hitesh")
    # formatted print
    print("Formatted string")
    name = 'Hitesh'
    surname = 'Pandey'
    print(f"My name is {name} {surname}")

    # Python print will always print in new line, to disable new line we can do this
    print("print line 1 without break. ", end=" ")
    print("print line 2")

    # Print multile values with ',' comma. This will auto add a ' ' spearator between values
    print("Print multiple values on a line with comma")
    print("Hi", "This is separated", "values")


def get_variable_operations():
    """
    Runs all scenarios of variable operations
    """

    # Assignment
    # In python variable assignment is simply done as a = b
    variable = 1

    # Operator * operation on string to numerical
    # Python doesn't give error in this case
    # It will instead print * ten times
    print("Multiplying 10 with * string", '*' * 10)
    # Same for + it wil concatenate string
    print("Adding a + a : ", "a" + "a")

    print("Unassinging/deleting a variable")
    # A varaible can simply be unassigned and emptied by using del
    varaible = 12345
    del varaible
    # This will give error since varaible doesn't exist anymore
    # print(varaible)

    # ADD
    print("Add: 2 + 1  ", 1 + 2)
    # Subtract
    print("Substract 5-4: ", 5 - 4)
    # Multiply
    print("Multiply 2*2: ", 2 * 2)
    # Divide
    print("Divide 2/2: ", 2 / 2)
    # Divide without auto decimal points rounded values
    print("Divide 2//2: ", 2 // 2)
    print("Divide 2//3: ", 2 // 3)
    # Raise to / Power
    print("Power 2**3", 2 ** 3)
    # Mod
    # Returns remainder of the division
    print("Mod operator", 3 % 2)

    # Variable increment
    value = 2
    value = value + 2
    # We take the value that is aready 2 and add two to it
    # The code execution is done from right to left
    # Hence this is possible, the value= will exist or read only after value + 2 is done

    # Shorthand icrement
    # The above can aslo be written as
    # This does the same increment value by 2
    value += 2
    print("Value increment by 2 and 2 again", value)
    '''
        !- Same can be done for - + / * and other operations
    '''

    # BODMAS (Bracket. Exponentioal/root. Division. Multiplication. Substraction) in prority order
    x = 2 + 3 * (4 + 8) / 2 - 16 + 2**2
    print("Bodmas operation on '2 + 3 * (4 + 8) / 2 - 16 + 2**2' ", x)


def get_math_operations():
    """
    Runs all scenarios of math operatoins
    """
    """
    For math function we need to import Math module
    """
    # Absolute values, it return a positive value, so it always return positive value
    x = -50
    abs(x)

    # Ceil to get decimal value to nearest rounded higher number
    print("Ceil method to 2.9 ", math.ceil(2.9))

    # floor to get decimal value to nearest rounded lower number
    print("floor method to 2.9 ", math.floor(2.9))

    """
    Note:- for more math operatoins see 
    https://docs.python.org/3/library/math.html
    """


def get_user_input():
    """
    Really basic method to get user input from terminal
    """
    # This is really useful for creating a command line program
    name = input('Enter nane')
    print(f'Hi {name}')
    color = input('Enter your favorite color')
    print(f'{name} like {color}')

