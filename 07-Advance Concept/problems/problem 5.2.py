def NegativeNumberError(Exception):
    pass

try:
    num = int(input('Enter a number: '))

    if num<0:
        raise NegativeNumberError('number canot be negative')
    result = num/45
except ValueError:
    print('only number not string')
except ZeroDivisionError:
    print('Not divisible by zero')
except NegativeNumberError as e:
    print(f'error : {e}')
