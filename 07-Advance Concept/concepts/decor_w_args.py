def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)

        return wrapper
    return decorator

@repeat(5)   
def hello(a):
    print(f'Hello! {a}')


hello('shakti')


for i in range(10):
    print('sya hello')


