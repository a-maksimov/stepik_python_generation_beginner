filename = 'numbers.txt'

with open(filename, encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]
    numbers = [[int(number.strip()) for number in line.split() if number.strip().isdigit()] for line in lines]
    sums = [sum(ls) for ls in numbers]
    print(*sums, sep='\n')


# with open('numbers.txt') as f:
#     for line in f:
#         print(sum(map(int, line.split())))