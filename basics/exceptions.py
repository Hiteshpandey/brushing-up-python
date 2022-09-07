"""
Note:- Python returns an exit code on executions
This should be 0
if exit code is other than 0, this means that the execution of the script caused an error
"""

# We use try catch to handle an exception
# An exception is raised by python or a particular python library when an invalid operation is done or an invalid value is being passed.

# try consists of the code that we are trying to execute and catch any error if that happens
# except block is executed the instant any code block in the try catch causes an error or exception
# Try block exectuion is haled and exited from the line that causes the error, so the below code won't be executed. 
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
# Value error exception is the exception raised by python if an operation on an invalid type is done.
# in the except block we can catch any kind of error and handle it, to notify or log the operation issue
except ValueError:
    print('Invalid value for age, it should be an number')
# we can chaing the exception handling for multiple types of exception
except ZeroDivisionError:
    print('Age cannot not be zero')

# If we don't use try except block we will have an issue with the script dying on the error code
# without any indication no the production code
# also it might halt other operation done after the code, maybe other funcitons written below won't be executed.
# with try except it will do necessary thing with the except block and will continue operation