def decorator(func):
    def wrapper():
        print('i am before')
        func()
        print('I am executed the code func')
    return wrapper


@decorator
def hello():
    print('hello')


hello()
# f = decorator(hello)
# f()

