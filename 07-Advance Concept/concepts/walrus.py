# while(data:=input('inter number and anything:- ')):
#     print(data)
#     if data == 'q':
#         break



# data = input('inter a value (or quit to exit):- ')

# while data != 'quit':
#     print(f'data is {data}')
#     data = input('inter a value (or quit to exit):- ')


# while (data := input('inter a value (or quit to exit):- ')):
#     print(f'data is {data}')
#     if data == 'q':
#         break

    

# numbers = [1, 2, 3, 4, 5]
# without walrus.

# results = [x * 2 for x in numbers if x*2 > 5]
# print(results)

# results = [y for x in numbers if (y:= x * 2) > 5]
# print(results)


# with open('text.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         print(line.strip())
#         line = f.readline()

with open('text.txt', 'r') as f:
    line = f.readlines()
    print(line)