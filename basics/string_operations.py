def run_string_operations():
    """
    Run a set of string operations in python
    """
    string = "Hello world"
    # string characters can be seeked by using array like index acess staring from 0
    print(string[0])
    # negative -1 means it will start at the starting index from end of the string
    print(string[-1])
    print(string[-2])

    # getting a section from a string can also be done using slice method
    # [start: stop]
    print(string[0:4])

    # string concatenation can be done simply with the + operator
    print("Hi" + ' ' + 'There')

    # copy or clone a string
    # start and endpoint is auto assumed to be 0 and end of the string this time
    # this retuns the entire string
    string2 = string[:]
    print(string2)
