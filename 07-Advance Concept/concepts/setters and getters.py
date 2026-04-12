# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     @property
#     def first_name(self):
#         l =  self.name.split(' ')
#         # print(l)
#         return (l[0])
#     @first_name.setter
#     def first_name(self, first):
#         l =  self.name.split(' ')
#         new_name = f'{first} {l[1]}'
#         self.name = new_name


# e = Employee('jack doe', 45535)
# # print(e.first_name())
# # e.set_first_name('Jhon')
# # print(e.name)


# print(e.first_name)
# e.first_name = 'Jhon'
# print(e.name)




# e.property = 6
# print(e.property)






# Traditional Apporach.
# class Person:
#     def __init__(self, name):
#         self._name = name
        
#     def get_name(self):
#         return self._name
    
#     def set_name(self, new_name):
#         self._name = new_name

# p = Person('Alice')
# print(p.get_name())
# p.set_name('Bob')
# print(p.get_name())






# class Person:
#     def __init__(self, name):
#         self._name = name
#     @property  
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name

# p = Person('Alice')
# print(p.name)
# p.name = 'Bob'
# print(p.name)



# print(p.get_name())
# p.set_name('Bob')
# print(p.get_name())



# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius
    
#     @property
#     def area(self):
#         return 3.144 * self._radius * self._radius
        
# c = Circle(10)
# print(c.area)
# print(c.radius)




