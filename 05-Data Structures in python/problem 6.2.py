# products = {
#     'apple' : 49,
#     'guava' : 55,
#     'banana' : 39,
#     'chilli' : 100
# }


# highest_product = max(products, key=products.get)

# print(highest_product, ':', products[highest_product])




# # for values in products.values():
# #     if values >=
# #     print(values)

# # max()

# # highest_price = max(products, )

# highest = (max(products, key=products.get))
# print(f'{products}, {}')







# # numbers = [3, 7, 2, 9, 5]
# # print(max(numbers))

# words = ["apple", "banana", "kiwi"]
# print(max(words, key=len))




numbers = [3, 7, 2, 9, 5]

max_num = numbers[0]

for i in numbers:
    if i > max_num:
        max_num = i

print(max_num)
    