def listaker(number):
    '''
    Removes all duplicates.

    parameters
        numbers (list)
    '''
    return list(set(number))

nums = [1, 2, 3, 4, 5, 6, 1, 2 , 5, 6]
print('Original nums', 1)
print('remove duplicates',listaker(nums))