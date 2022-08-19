def run_string_operations():
    """
    Run a set of string operations in python
    """
    string = "Hello world"
    # String characters can be fetched by using array like index access staring from 0
    print("Sliced strings")
    print(string[0])
    # -1 means it will start at the starting index from end of the string
    print(string[-1])
    print(string[-2])

    # Getting a section from a string can also be done using slice method
    # [start: stop]
    print(string[0:4])
    print(string[1:-1])

    # LENGTH of string
    print("length of string: ", len(string))

    # String CONCATENATION can be done simply with the + operator
    print("Hi" + ' ' + 'There')

    # COPY or CLONE a string
    # Start and endpoint is auto assumed to be 0 and end of the string this time
    # This returns the entire string
    string2 = string[:]
    print("copied string: ", string2)

    # CAPITALIZE the text
    print('capitalize string: ', string.capitalize())
    # same
    print('capitalize string: ', string.title())

    # LOWERCASE string
    print("lowercase string: ", string.casefold())
    # Same
    print("lowercase string: ", string.lower())

    # UPPERCASE string
    print("upper case stirng: ", string.upper())

    # COUNT OCCURRENCE of the specific word
    print("count times ld occurred in the string: ", string.count('ld'))

    # Encode a string (usually required to convert bytes string to human-readable form or from one unicode to other)
    # This mutates/updates the original string
    # Unicode string
    ustring = 'pythön!'
    print("unicode string : ", ustring)
    # Default encoding to utf-8
    print("utf8 encoded: ", ustring.encode())
    # ascii
    # Commented due to throwing errors, which the below two definintions fix
    # ustring = 'pythön!'
    # print("ascii encoded: ", ustring.encode('ascii'))
    ustring = 'pythön!'
    print("ascii encoded (ignore error): ", ustring.encode('ascii', 'ignore'))  # To ignore error
    ustring = 'pythön!'
    print("ascii encoded: (replace error)", ustring.encode('ascii', 'replace'))  # To replace error character with ?

    # Check if string ends with a certain word
    # It returns True if a string ends with the specified suffix.
    # It returns False if a string doesn't end with the specified suffix.
    message = 'Python is fun'
    print('Message string: ', message)
    print('Message string end with fun or not: ', message.endswith('fun'))

    # Search/Find a substring
    # Shorthand way of finding string
    print("Short hand find Python in string", 'Python' in message)

    # returns -1 if not found
    message = 'Python is a fun programming language'
    print('Message string: ', message)
    # check the index of 'fun'
    # returns index of search
    print('Message string "fun" index: ', message.find('fun'))

    # Find index of a substring
    # Raises exception if string not found
    txt = "Hello, welcome to my world."
    print('Message string: ', txt)
    x = txt.index("welcome")
    print('word "welcome" index: ', x)

    # Removing leading or trailing space
    txt = "     banana     "
    print('Message string: ', txt)
    # Leading space
    x = txt.lstrip()
    print('lstrip string: ', x)
    # Trailing space
    x = txt.rstrip()
    print('lstrip string: ', x)
    # Leading and trailing spaces
    x = txt.strip()
    print('strip string: ', x)

    # Split string to list
    txt = "welcome to the jungle"
    print('Message string: ', txt)
    # Split with spaces (space is the default when nothing is specified)
    x = txt.split(" ")
    print('String split into array: ', x)

    # Search and replace string
    print("Search and replace jungle with palace")
    txt = "welcome to the jungle"
    print("message string : ", txt)
    print("Replaced string :", txt.replace('jungle', 'palace'))


