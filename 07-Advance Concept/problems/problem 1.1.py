def logger(func):
    def wrapper(*args, **kwargs):
        print('Function is being called.')
        return func(*args, **kwargs)
    return wrapper

@logger
def say_hello(a):
    print(f'Hello! {a}')

say_hello('shakti')