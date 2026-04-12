# def greet(name):
#     return f'Hello, {name}!'

# print(greet('shakti'))

# number = [1, 2, 3, 4]

# squred = list(map(lambda x : x**2, number))
# print(squred)


# num = 5
# fact = 1

# for i in range(1, num+1):
#     fact *= i
# print(fact)


# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

# fib of any number 

# fib(n) = fib(n-2) + fib(n-1)

# def fib(n):
#     if (n == 0 or n == 1):
#         return n
    

#     return fib(n-2) + fib(n-1)
# print(fib(0))


# local variable and global variable.

# a = 10  # global variable

# def sum(a, b):
#     c = a+b
#     a = 32  # local variable
#     return c

# print(a)
# print(sum(10, 20))




# def sum(a, b):
#     print('i am summing')
#     c = a+b
#     global z
#     z = 0
#     return c

# z = 3

# print(sum(10, 20))
# print(z)



# def add(a, b):
#     ''' the add the two number'''
#     return a + b

# print(add(10, 40))