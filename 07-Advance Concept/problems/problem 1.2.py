from time import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result =  func(*args, **kwargs)
        end = time()
        print(end - start)
        return result
    return wrapper



@timer
# start = time.time()
def total_sum(*args):
    total = 0
    for i in args:
        total += i
    return total

a = total_sum(323, 43, 3434)
print(a)

# print(total_sum.__name__)




# print(sum(range(1000001)))

# n = 1000000
# print( n *(n+1) // 2)



# print( 5 / 2)  # returns float 
# print( 5 // 2)  # returns int 
