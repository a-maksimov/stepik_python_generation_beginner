# put your python code here

string1 = input().lower()

string2 = input().lower()

dict1 = {}
for letter in string1:
    if letter.isalpha():
        dict1[letter] = dict1.get(letter, 0) + 1

dict2 = {}
for letter in string2:
    if letter.isalpha():
        dict2[letter] = dict2.get(letter, 0) + 1

if dict1.items() == dict2.items():
    print('YES')
else:
    print('NO')