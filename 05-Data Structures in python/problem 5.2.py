mydict = {
    'sumit' : 33445566775544,
    'rohit' : 445566770044,
    'mohit' : 4353323445544
}


print(mydict.keys())
print(mydict.values())
print(mydict.items())


for keys, value in mydict.items():
    print(keys, ':', value)