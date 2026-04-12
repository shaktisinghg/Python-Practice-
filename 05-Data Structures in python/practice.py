 
# fruits = ["apple", "banana", "cherry"] 

# print(fruits[0])
# fruits.repl
# print(len(fruits))


# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(n[0:3])
# print(n[-1:-4:-1])


 

# numbers = [5, 2, 9, 1, 7]
# numbers.sort()
# numbers.append(10)
# numbers.remove(2)

# print(numbers)




# names = ["Alice", "Bob", "Charlie"]
# names.insert(1, 'David')
# print(names)



# cordinates = (10, 20)

# t_to_l = list(cordinates)
# t_to_l[0] = 50
# l_to_t = tuple(t_to_l)
# print(l_to_t)
# print(cordinates)




# my_set = {1, 3, 2, 3, 4, 2}
# my_set.add(5)
# my_set.remove(2)
# print(my_set)





# student = {"name": "John", "age": 20, "grade": "A"}

# # print(student["name"])
# # student["grade"] = 'A+'
# # student['City'] = 'New Work'
# # print(student)
# student.pop('name')
# student.clear()
# print(student.keys())
# print(student.values())
# print(student.items())







# num = list(input('inter number'))

# s_num = set(num)
# print(s_num)



product = {'apple': 50,
           'guava' : 60,
           'banana' : 30}

cutlery = {
    "glass" : 30,
    'plate' : 50
}

# a = product + cutlery
# print(a)

for i in product:
    print(product[i])