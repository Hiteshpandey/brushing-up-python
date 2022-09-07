class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'My name is {self.name}')


hitesh = Person('Hitesh Pandey')
hitesh.talk()

bob = Person('Bob Jones')
bob.talk()