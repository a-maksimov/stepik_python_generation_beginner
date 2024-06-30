filename = 'data.txt'

with open(filename, encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]
    lines.reverse()
    print(*lines, sep='\n')