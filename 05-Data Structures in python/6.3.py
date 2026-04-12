# solution 1 

def merge_dicts(dict1, dict2):
    '''
    Merge two dictionaries into one

    parameter
        dict1 (dict) : first dictionary
        dict2 (dict) : second dictionary

    return
        dict: A new dictionary with combined key-value pairs.
    '''
    return {**dict1, **dict2}

d1 = { 'a' : 1, 'b' : 2}
d2 = {'c' : 3, 'd' : 4}

merged = merge_dicts(d1, d2)
print(merged)

# solution 2 

d1.update(d2)
print(d1)