# put your python code here

n = int(input())

dict = {}

for _ in range(n):
    string = input().split()
    name, product, number = string[0], string[1], int(string[2])
    dict[name] = dict.setdefault(name, {})
    dict[name].update({product: dict[name].get(product, 0) + number})

for name in sorted(dict):
    print(name + ':')
    for product in sorted(dict[name]):
        print(product, dict[name][product])

