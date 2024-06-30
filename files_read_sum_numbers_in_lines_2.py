filename = 'nums.txt'

with open(filename, encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        for sym in lines[i]:
            if sym not in '0123456789':
                lines[i] = lines[i].replace(sym, ' ')
    print(sum([sum(map(int, line.split())) for line in lines]))

# прогуляться по каждому символу в тексте
# with open('numbers.txt', encoding='utf-8') as file:
#     row = ''.join(c if c.isdigit() else ' ' for c in file.read())
#     print(sum(map(int, row.split())))