# try:    
#     file = open('my_file.txt' 'r')
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print('file not exist')




# try:    
#     file = open('my_file.txt' 'r')
#     for line in file:
#         print(line.strip())
#     file.close()
# except FileNotFoundError:
#     print('file not found for read')




# file = open('new_file.txt', 'w')
# file.write('this is first line!\n')
# file.write('this is second line!\n')
# file.close()


# file = open('new_file.txt', 'a')
# file.write('this is appended text.\n')




# try:    
#     file = open('new_file.txt', 'r')
#     for line in file:
#         print(line.strip())
#     file.close()
# except FileNotFoundError:
#     print('file not found for read')




try:    
    with open('E:\s.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print('file not found for read')



  
# with open('new_file2.txt', 'w') as f:
#     f.write('name is shakti singh.\n')
