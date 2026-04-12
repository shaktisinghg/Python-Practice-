import argparse

# parser = argparse.ArgumentParser(description="simple calculator")

# parser.add_argument('num1', type=float, help='first number')
# parser.add_argument('num2', type=float, help='second number')
# parser.add_argument('operation', choices=['add', 'sub', 'mul', 'div'], help='operation here')

# args = parser.parse_args()
# # print(args)
# try:
#     if (args.operation == 'add'):
#         print(f'The result is {args.num1 + args.num2}')

#     elif (args.operation == 'sub'):
#         print(f'The result is {args.num1 - args.num2}')

#     elif (args.operation == 'mul'):
#         print(f'The result is {args.num1 * args.num2}')

#     elif (args.operation == 'div'):
#         print(f'The result is {args.num1 / args.num2}')
#     else:
#         print('some error occured')
# except Exception as err:
#     print(f'error is :{err}')








parser = argparse.ArgumentParser(description="simple calculator")

parser.add_argument('filename', help='The file to process')
parser.add_argument('-n','--number', type=int, default=1, help='Enter number of times to open file')

args = parser.parse_args()

try:
    with open(args.filename, 'r') as f:
        content = f.read()
        for _ in range(args.number):
            print(content)
except Exception as err:
    print(f'error is : {err}')




# parser = argparse.ArgumentParser()

# parser.add_argument('name')
# parser.add_argument('age')

# args  = parser.parse_args()

# print(args.name)
# print(args.age)



# with open('new.txt', 'w') as f:
#     f.write('shakti singh command line utility.')