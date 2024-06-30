# put your python code here

n = int(input())

dict = {}

commands = {'R': 'read', 'W': 'write', 'X': 'execute'}

for string in range(n):
    string_list = input().split()
    filename = string_list[0]
    access = set([commands[command] for command in string_list[1:]])
    dict[filename] = access

m = int(input())

for string in range(m):
    string_list = input().split()
    filename = string_list[1]
    if string_list[0] in dict[filename]:
        print('OK')
    else:
        print('Access denied')

