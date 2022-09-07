class Mammal:
    def __init__(self, animal):
        self.animal = animal
    def walk(self):
        print(f'{self.animal} is walking')

# Inheritance by passing Mammal as a parent to dog class
# This makes dog to be able to access everything in the parent Mammal class
class Dog(Mammal):
    def __init__(self, name):
        self.name = name
        # But now how can we invoke parent constructor and pass animal as dog?
        # Initialize parent constructor and pass dog as an animal type
        # We can do that using super() method that refers to the parent class
        super().__init__('Dog')
    
    def get_name(self):
        print(f"Dog's name is {self.name}")

class Cat(Mammal):
    def __init__(self, name):
        self.name = name
        # But now how can we invoke parent constructor and pass animal as dog?
        # Initialize parent constructor and pass dog as an animal type
        # We can do that using super() method that refers to the parent class
        super().__init__('Cat')
    
    def get_name(self):
        print(f"Cat's name is {self.name}")

dog1 = Dog('Fido')
dog1.walk()
dog1.get_name()

cat1 = Cat('Milli')
cat1.walk()
cat1.get_name()