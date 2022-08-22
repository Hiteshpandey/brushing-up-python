# Command line arguements are the paraemteres or values that provide your code through terminall commands

# The sys package gives us the sys.arv property
# This consist of all of the parameters that are passed to this file
# eg. command_line_arguements.py param1 param2 param3

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
appended = ""
# Using argparse module
for i in range(1, n):
    appended += ' | ' + sys.argv[i]
     
print("\n\nResult:", appended)
