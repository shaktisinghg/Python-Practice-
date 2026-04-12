class Employee:
    company = 'Apple'

    def show(self):
        print(f'The name is {self.name} and the company is {self.company}')

    @classmethod
    def changecompany(cls, newcompany):
        cls.company = newcompany


e1 = Employee()
e1.name = 'shakti'
print(e1.name)
e1.show()
e1.changecompany('Tesla')
print(e1.company)
e1.show()
print(e1.company)