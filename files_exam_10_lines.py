with open('lines (2).txt', 'r', encoding='utf-8') as file:
    lines = []
    line = file.readline()
    while line != '':
        lines.append(line.strip())
        line = file.readline()

if len(lines) < 10:
    print(*lines, sep='\n')
else:
    print(*lines[len(lines) - 10:len(lines) + 1], sep='\n')