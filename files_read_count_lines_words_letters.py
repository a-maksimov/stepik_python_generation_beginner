filename = 'file.txt'

with open(filename, encoding='utf-8') as file:
    lines = file.readlines()
    linesnum = len(lines)
    wordsnum = sum(list(map(lambda line: len(line.split()), lines)))
    letternums = [[1 for sym in str(line) if sym.isalpha()] for line in lines]
    lettersnum = 0
    for elem in letternums:
        lettersnum += sum(elem)
    print('Input file contains:')
    print(f'{lettersnum} letters')
    print(f'{wordsnum} words')
    print(f'{linesnum} lines')

# with open('lines.txt') as f:
#     txt = f.read()
#     print('Input file contains:')
#     print(sum(map(str.isalpha, txt)), 'letters')
#     print(len(txt.split()), 'words')
#     print(txt.count('\n') + 1, 'lines')