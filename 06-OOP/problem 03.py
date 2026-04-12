class Animal:
    def sound(self):
        print('some sound')

class Dog(Animal):
    def sound(self):
        print('Bark!')

dog1 = Dog()
dog1.sound()