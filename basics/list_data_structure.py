# python provides various predefined data structures so that we can organize our data better

def run_list_data_structure_operations():
    """
    runs several operations on list data structure
    """
    # list is a sequential storage
    # this stores a list of data in sequential order
    # mixed data types can be used like string, in, boolean and also other data structures like tuple
    # the list is mutable which means, once created elements can be added, updated and deleted from the list.
    my_list = [1, 2, 3, 4, 5]
    print('list: ', my_list)

    # APPEND
    """
    Adds element to the END of the list
    """
    print("Append to list 6")
    my_list.append(6)
    print("Append to list 7")
    my_list.append(7)
    print("Append to list 8")
    my_list.append(8)
    print("Appended list: ", my_list)

    # INSERT
    """
    Add a single element at the given index of the list
    It will insert the element on the provided index and shift all the elements on the right to right
    Elements will not be deleted
    """
    print("Insert to list")
    # myList.insert(index, element)
    my_list.insert(2, 'element')
    print("Insert 'element' on the 2th index: ", my_list)

    # POP
    # Remove element from the list from the provided index and returns it
    # By default deletes the end element and returns it
    print("Pop element from end of list, popped element", my_list.pop())
    # Remove element on the 3rd index
    print("Pop element from 3rd index of list, popped element", my_list.pop(3))

    """
    # REMOVE
    Remove the provided element from the list
    """
    my_list.remove('element')
    print("Removed element 'element'", my_list)

    """
    FIND a value exist or not
    this can be simply done using in keyword
    """
    print('check if "element" string is in the list', 'element' in my_list)
    print('check if 9 value is in the list', 9 in my_list)

    """
    # SLICING
    # my_list[start_index: stop_before_index]
    """
    print("Slicing of the list")
    print(my_list[:2])
    print(my_list[1:4])
    print(my_list[1:])
    # returns everything
    print(my_list[:])

    """
    # REVERSE LIST
    # START default i.e 0, END default i.e end of the list and -1 that is reverse steps incremented by one
    # Returns the new list
    """
    print("Reversing list")
    print(my_list[::-1])
    # Updates the original list
    my_list.reverse()
    print("By reversed method mutating list")
    print(my_list)

    # LENGTH / SIZE OF LIST
    print("Length of the list")
    print(len(my_list))
    
    # GET INDEX OF THE ELEMENT
    # If number not in the list, it will give value error
    print(my_list.index(2))

    # COUNT NUMBER OF ELEMENTS REPEATED IN THE LIST
    my_list.push(10)
    my_list.push(10)
    print(my_list.count(10))

    # MIN MAX VALUE
    print("Max and min value in the list")
    # finds the minimum or max values from the list
    # Better works on the list with only one type (homogeneous) of elements
    print(min(my_list))
    print(max(my_list))

    # CONVERT TUPLE TO LIST
    tpl = (1, 2, 3, 4)
    lst = list(tpl)
    print("list : ", tpl)
    print("list to tuple: ", lst)

    # 2D LISTS
    # This can be seen as list inside of list
    # And represented as a grid or a mathematical matrix
    # Very useful for data that requires two or more value to represent
    # Eg such as (x,y) axis, displacement distance points, graphs etc.
    """
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    """

    matrix = [
        [1, 2, 3],
        [4, 5, 6, 6],
        [7, 8, 9],
    ]

    print("2D Lists", matrix)
    print("2D First row", matrix[0])
    print("2D first element from the first row", matrix[0][0])
    print("Number of rows: ", len(matrix))
    print("Number of columns in the first row", len(matrix[0]))
    print("Number of columns in the second row", len(matrix[1]))

    print("Looping over matrix")

    for row in matrix:
        # the i will contain list of items in first row
        print("Printing first row elements")
        for i in range(len(row)):
            print(f"{i} element: ", row[i])
