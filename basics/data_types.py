# This will consist of basic varaible types assignment in python
# Variables are case sensitive in python

def print_native_data_types():
    """
    prints variable operations
    """
    # python auto assigns types in background similar to php
    # every variable we create in python is created as an object in the background
    # so we can say that almost everything created in python is an object
    # price = 10 is not natively assigned it is saved as an encapsulated object

    # this is an integer type assignment
    price = 10
    # this proves that the price type is an int type class
    # print(type(price))
    print("int: ", price)

    # floating type. This is 64 bit precision floating point
    # Double type in C
    percentage = 12.0984
    print("float: ", percentage)

    # Boolean types are binary values of True or False
    # Note:- True False are capitalized
    onoff = False
    print("boolean: ", onoff)

    # String type in python
    # single or double quotes doesn't matter
    # string should be single line only and cannot break
    name = "Hitesh"
    print("String: ", name)

    # raw pyton string is a literal string
    # it can be anything ranging from html with having long text with slashes and multiple character symbols
    # data inside the raw string wouldn't be parsed by the python interpreter so \/ \n \t wouldn't have any menaning
    raw_html = r'Hi \ / ` there \n \t'
    print("raw String: ", raw_html)

    # triple quotes can be used to write string in multiline
    multiline = """line one
    line two
    line three"""
    print("multiline: ", multiline)

    # complex number type is used for representing math equations with complex number like root -1
    # imaginary number can be denoted with j
    cpx = (2 + 3j)
    print(type(cpx))
