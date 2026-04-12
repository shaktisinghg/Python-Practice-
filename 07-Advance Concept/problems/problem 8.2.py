# def print_details(**kwargs):
#     for d in kwargs:
#         print(f'{d} : {kwargs[d]}')

# print_details(name='shakti', age = 40)




def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_details(name='shakti', age = 40)