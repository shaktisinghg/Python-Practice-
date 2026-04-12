from functools import wraps

# def universal(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'you are calling : {func.__name__}')
#         print(f'you arguments : args={args}, kwargs={kwargs}')
#         a =  func(*args, **kwargs)
#         print(a)
#         return a
#     return wrapper
    
# @universal
# def add(a, b):
#     print( a + b)

# add(10, 20)


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    '''saying hello'''
    print('Hello!')

print(greet.__name__)
print(greet.__doc__)
greet()



# functools.wraps is a decorator in Python used when you’re writing your own decorators. Its job is to make the wrapped function look like the original function instead of losing its identity.

# The problem it solves

# When you decorate a function, the original function gets replaced by the wrapper. Without wraps, important metadata is lost:


def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Say hello"""
    print("Hello")

print(greet.__name__)  # wrapper
print(greet.__doc__)   # None