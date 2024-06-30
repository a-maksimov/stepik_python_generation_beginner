filename = 'lines (1).txt'

with open(filename, encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]
    lens = list(map(len, lines))
    lines_filtered = list(filter(lambda line: len(line) == max(lens), lines))
    print(*lines_filtered, sep='\n')




