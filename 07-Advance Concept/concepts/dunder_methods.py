# class Employee:
#     company = 'HP'
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return f'your name is {self.name} and salary is {self.salary}'
    
#     def __len__(self):
#         return len(self.name)

# e = Employee('Alice', 34433)
# print(e.name, e.salary)
# print(e.__str__())
# print(len(e))
# print(len(e.name))




class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __str__(self):
        return f'vector {self.x}, {self.y}'
        
a = Vector(1, 4)
b = Vector(5, 3)

c = a + b
print(c)

