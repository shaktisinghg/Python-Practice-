class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property   # this is the getter   It lets you access a method like an attribute.
    def salary(self):
        return self._salary
    
    @salary.setter  # this is the setter
    def salary(self, value):
        if (value < 0):
            print('hey please dont send 0 or negative value for salary')
        else:
            self._salary = value
        
e = Employee('5000')
print(e.salary)
e.salary = 500083748
print(e.salary)