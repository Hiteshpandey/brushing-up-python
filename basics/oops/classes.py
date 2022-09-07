# Classes can be used to define complex real wolrd types and relationsip
# We are basically representing real world data concepts and relationships

# Note:- For people who are form another oop language
# Filename doesn't relate to a class defined in python
# So file of a file containing a class can have a different name and contain multiple classes
# Look -> https://dirtsimple.org/2004/12/python-is-not-java.html

# Class is a blue print to create an object. which is created by passing data to a class
# So a object is a class that is personified by a data and every different data pass will create a new instance of a class with that data.
# Keyword class , class name Point -> pascal naming convention which is First letter should be upper case and every othr letter starts wit uppercase letter
class Point:
    # __init__ :- is aConstructor, this basically runs first, everytime when an object is intiated/created
    # Self is as the name states, is a reference to the class itself
    # Self :- Using self we can access/modify/assign any method or attributes inside the class anywhere. By just doing self.attribute/method
    def __init__(self, x, y):
        # Assign passed values to attributes when initializing an object
        self.x = x
        self.y = y
    # Method move
    def move(self):
        print('move')
    # Method draw
    def draw(self):
        print(f'drawing {self.x} {self.y}')

# Create an object
point1 = Point(11, 12)
# create new attributes, basically values for the class instance
point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)
# call a method
point1.draw()

point2 = Point(12, 45)
print(point2.x)
print(point2.y)

# Note:- For people from other languages
# python doesn't autocall default __init__() constructor when no value is passed in the initialization
# Python does not support Constructor overloading
# It needs the values passed everytime unless we specify default values for the constructors 

