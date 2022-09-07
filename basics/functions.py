# Functions are small block of resuable codes that can be used anywhere conveniently
# In python function is defined by def key word followed with function name and () ending with :
# It's a good practice to provide docstring info for each function explaining what it does and what it requires
# Note:- docstring startin with !-- are my notes not the docstring parameters

def a_fuction_that_prints_hello():
    """
    !-- This is called a doc string, it consists of all the information about the method/class/function we are creating
    Prints a hello world function
    """
    print('Hello')


def add_print_function(a, b):
    """
    Basic add function that adds two numbers
    Parameters:
    :param a: (int) first number
    :param b: (int) second number
    """
    print(a + b)


def add_function(a, b) -> int:
    """
    Basic add function that adds two numbers
    Parameters:
    :param a: (int) first number
    :param b: (int) second number
    :return: (int) additoin result
    """
    return a + b


# For non retun value we just don't specify anything in return
def typed_add_function_print(a: int, b: int): 
    """
    Basic add function that adds two numbers
    Parameters:
    :param a: (int) first number
    :param b: (int) second number
    :Returns:
    :return: (str) addition result
    """
    # typecasting so as to make return type string
    print(str(a + b))

# Passing arguements
print(typed_add_function_print(1, 2))

# We can pass named parameters by passing expected variable names in the calling functions
# We can specify value on the paramters to make it opitional, in this case operator parameter
def typed_operation_function(a=2, b=1, operator=None):
    if operator == '+':
        return a+b
    if operator == '-':
        return a-b
    if operator == '/':
        return a/b
    if operator == '*':
        return a*b
    else:
        return a+b

"""
Note:-
We can also use keyword or positional arguements
But take in mind the position of the arguement will take preceedence over the keword arguements
"""

# Passing list
def list_print_function(*argv):
    for data in argv:
        print(data)

def dict_print_function(**kwargs):
    for key, value in kwargs.items():
        print(f"key {key}, value {value}")

print(typed_operation_function(5, 4, '-'))

list_print_function(1, 'asdf', True, {'name': 'hitesh'})

dict_print_function(name='Hitesh', lastname='Pandey')
