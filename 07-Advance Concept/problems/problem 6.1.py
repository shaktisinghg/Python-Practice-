# c = [1, 2, 3, 4, 5]

# cubes = list(map(lambda x : x*x*x, c))
# print(cubes)



# e = [10, 11, 12, 13, 14]

# even = (filter(lambda x : x%2 == 0, e))
# print(list(even))



from functools import reduce
p = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x*y, p)
print(result)
