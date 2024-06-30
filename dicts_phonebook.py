# put your python code here

n = int(input())

dict = {}

for _ in range(n):
    string = input().split()
    key, value = string[1].lower(), string[0]
    dict[key] = dict.setdefault(key, [])
    dict[key].append(value)

m = int(input())

for _ in range(m):
    name = input().lower()
    if name in dict.keys():
        print(*dict[name])
    else:
        print('абонент не найден')

# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))
