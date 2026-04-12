def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper
    
def exclaim(func):
    def wrapper():
        return func() + '!!!'
    return wrapper


    
@exclaim
@uppercase
def hello():
    return 'hello'




print(hello())