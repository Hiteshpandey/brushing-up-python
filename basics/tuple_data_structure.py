def tuple_data_structure():
    """
    runs several operations on tuple data structure
    """
    # tuple is a sequential storage like list but is immutable
    # this means it cannot be updated once it is created
    tupllist = (1, 2, 3, 4, 5)
    print('list: ', tupllist)
    print("Third item: ", tupllist[2])

    """
    Get index of the first occurance in tuple
    """
    print("First occurance of 3")
    print(tupllist.index(3))

    """
    Appending:
    Tuples cannot be modified but can be appended to another tuple
    """
    print("Append two tuples")
    tupllist2 = (6, 7, 8, 9)
    print("Tuple 2", tupllist2)
    newtup = tupllist + tupllist2
    print("Tupple after append : ", newtup)

    # Length of tuple
    len("Tuple length: ", len(tupllist))

    # Max Min
    print("Max value: ", max(tupllist), ". Min Value", min(tupllist))

    # Convert list to tuple
    lst = [1, 2, 3, 4, 5]
    print("Convert list to tuple")
    print("List: ", lst)
    print("List to tuple: ", tuple(lst))

    # Find value using in keyword
    print("Chck If 5 in tuple", 5 in tuple)

tuple_data_structure()