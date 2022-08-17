# functions are small block of resuable codes that can be used anywhere conveniently
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


def add_function(a, b):
    """
    Basic add function that adds two numbers
    Parameters:
    :param a: (int) first number
    :param b: (int) second number
    :return: (int) additoin result
    """
    return a + b


# Functions can also have typed inputs and return values
# this is called type hinting
def typed_add_function(a: int, b: int) -> str:
    """
    Basic add function that adds two numbers
    Parameters:
    :param a: (int) first number
    :param b: (int) second number
    :Returns:
    :return: (str) addition result
    """
    # typecasting so as to make return type string
    return str(a + b)

