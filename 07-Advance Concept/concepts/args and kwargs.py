# def My_function(*args):
#     print(type(args))
#     for arg in args:
#         print(arg)

# My_function('shakt', 10, 'mohit')


# for args

# def My_function(*args):
#     print(type(args))
#     for arg in args:
#         print(arg)

# My_function('shakt', 10, 'mohit')



# For Kwargs

# def My_function(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')

# My_function(name='shakti', clas = 10, )




# def my_function(a, b, *args, c=10, **kwargs):
#     print(f"a: {a}")
#     print(f"b: {b}")
#     print(f"args: {args}")
#     print(f"c: {c}")
#     print(f"kwargs: {kwargs}")

# my_function(1, 2, 3, 4, 5, c=20, name="Bob", country="USA")
# # Output:
# # a: 1
# # b: 2
# # args: (3, 4, 5)
# # c: 20
# # kwargs: {'name': 'Bob', 'country': 'USA'}

# my_function(1,2)
# # Output:
# a: 1
# b: 2
# args: ()
# c: 10
# kwargs: {}


# def M_function(a, b, *args, c=10, **kwargs):
#     print(f'{a}')
#     print(f'{b}')
#     print(f'{args}')
#     print(f'{c}')
#     print(f'{kwargs}')

# M_function(10, 20)





# use case of args and kwargs

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed, *args, **kwargs):
        super().__init__(name)
        self.breed = breed

        print(f'args : {args}')
        print(f'kwargs : {kwargs}')

dog1 = Dog('bhuli', 'german', 10, 20, nasl='dehati', age=10)