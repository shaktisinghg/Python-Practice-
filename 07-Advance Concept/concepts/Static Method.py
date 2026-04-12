class math:
    def __init__(self, num):
        self.num = num

    def addnum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b    
    
n = math(10)
n.addnum(5)
print(n.num)


print(n.add(10, 20))