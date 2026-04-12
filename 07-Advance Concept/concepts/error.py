
# try:
#     while True:
#         a = int(input('inter 1:- '))
#         b = int(input('inter 2:- '))
#         c = a + b
#         print(c)
#         if a == 'q':
#             break
# except Exception as err:
#     print(f'some error : {err}')



# try:
#     x = 10 / 0 # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     print("Cannot divide by zero!")


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except (ZeroDivisionError, ValueError) as e:
#     print(f'{e}')
# else:
#     print('divide ho gaya')
# finally:
#     print('ham hamesha print honge')


# file = None
# try:
#     file = open('type.txt', 'r')
#     content = file.read()
# except FileNotFoundError:
#     print('file not found')
# else:
#     print('file read successfully')
#     print(f'________file content_______\n{content}')
# finally:
#     if file:
#         file.close()




# def check_age(age):
#     if age < 18:
#         raise ValueError('Age must be 18 or older!')
#     return 'Access Granted.'



# # print(check_age(20))
# # print(check_age(18))
# print(check_age(17))




class InvalidAgeError(Exception):
    def __init__(self, message='Age must be 18 or older!'):
        self.message = message
        super().__init__(self.message)

def check_age(age):
        if age < 18:
             raise InvalidAgeError()
        return "Welcome!"
        
print(check_age(17))
    
        

