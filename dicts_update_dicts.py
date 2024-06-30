dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

dict1_copy = dict1.copy()

dict1.update(dict2)

for key in dict1.keys():
    if key in dict1_copy.keys() and key in dict2.keys():
        dict1[key] = dict1_copy[key] + dict2[key]

result = dict1




