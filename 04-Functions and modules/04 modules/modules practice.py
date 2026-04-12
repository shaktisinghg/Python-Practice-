# def greet():
#     print('Hello, Python Learner!')

# greet()




# def square(x):
#     return f'square of {x} is {x**2}'

# print(square(7))




# def full_name(first, last):
#     return first + " " + last

# print(full_name('shakti', 'singh'))



# def calculate_area(length, width=10):
#     return f'Area is {length * width}'

# print(calculate_area(10))
# print(calculate_area(10, 75))




# add = lambda x, y: x + y

# print(add(10, 20))




# f_list = [1, 2, 3, 4, 5]

# square = list(map(lambda x : x**2, f_list))
# print(square)



# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))


# def sum_of_digits(x):
#     sum = 0
#     for i in range(1, x+1):
#         sum += i
#     return sum

# print(sum_of_digits(3))


# import math

# a = int(math.sqrt(144))
# print(a)

# print(math.radians(90))


# import requests

# a = requests.get("https://api.github.com")
# print(a.json())



# def increment():
#     counter = 0
#     counter += 1
#     print(counter)

# increment()
# increment()
# increment()
# increment()
# increment()




# def multiply(a, b):
#     '''
#     Multiply two number 

#     parameters
#         a (int or float) : the first number.
#         b (int or float) : the second number.

#     returns
#         int or float: the product of a and b
#     '''
#     return a * b

# # print(multiply.__doc__)

# help(multiply)



# def safe_divide(a, b):
#     if b == 0:
#         return 'cannot divide by zero '
#     else:
#         return a / b
    
# print(safe_divide(10, 0))



# import my_utils

# print(my_utils.is_even(50))








# # fibonacci number.
# def fibonacci(n):
#     def fib(k):
#         if k<=1:
#             return k
#         return fib(k-1) + fib(k-2)

#     for i in range(n):
#         print(fib(i), end=' ')

# fibonacci(10)