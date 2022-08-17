# importing date class from datetime module for date opeartions
# So datetime is a package that is already avialbe to us from python library
from datetime import date


def calculate_birthdate():
    """
    Calculates the age from birth date
    """
    birth_year = input('Enter birth year')
    day = date.today()
    # day.year is a type integer but birth_year when taken from input is always a string
    # we need to convert birth year to a number type by using int typecasting which is short for integer
    # operations on different types are not permitted
    age = day.year - int(birth_year)
    print(age)
