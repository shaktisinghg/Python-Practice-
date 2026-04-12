# class Dog:
#     species = 'cannis familiaries'

#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f' dog is {self.name}')

# my_dog = Dog('lolo', 'german')
# print(my_dog.species)
# my_dog.bark()


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print('simple animal generic sound')

# class Dog(Animal):
#     def speak(self):
#         print('Woof!')

# class Cat(Animal):
#     def speak(self):
#         print('Mew!')


# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         super().__init__(name)
#         self.wingspan = wingspan

# my_bird = Bird('chidiya', 10)

# my_animal = Animal('buffalo')
# my_dog = Dog('german')
# my_cat = Cat('catuai')

# my_animal.speak()
# my_dog.speak()
# my_cat.speak()
# my_bird.speak()


# print(my_dog.name)
# print(my_cat.name)
# print(my_bird.wingspan)






# class Dog:
#     def __init__(self, name='unknown', breed='mixed'):
#         self.name = name
#         self.breed = breed

#     def show(self):
#         print(self.name, self.breed)

# dog1 = Dog()
# dog1.show()





class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, other):
        return point((self.x + other.x), (self.y + other.y))
    
    def print_point(self):
        print(f' x is {self.x} , y is {self.y}')

    def __add__(self, other):
            return point((self.x + other.x), (self.y + other.y))
    
    def __eq__(self, other):
         return self.x  == other.x and self.y == other.y    
    
    def __mul__(self, other):
         return ((self.x * other.x), (self.y * other.y))
         




p1 = point(2, 3)
p2 = point(2, 3)
p = p1 + p2
p.print_point()
print(p1 == p2)
# p = p1.sum(p2)
# p.print_point()
print(p1 * p2)