# put your python code here

n = int(input())

words = []
meanings = []

for _ in range(n):
    string = input()
    parsed = string.split(':')
    words.append(parsed[0].lower())
    meanings.append(parsed[1].strip())

prog_dict = dict(zip(words, meanings))

m = int(input())

for _ in range(m):
    string = input().lower()
    if string in prog_dict:
        print(prog_dict[string])
    else:
        print('Не найдено')


# mydict = {}
#
# for _ in range(int(input())):
#     key, value = input().split(': ')
#     mydict[key.lower()] = value
#
# for _ in range(int(input())):
#     print(mydict.get(input().lower(), 'Не найдено'))
