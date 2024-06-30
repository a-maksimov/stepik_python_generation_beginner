# put your python code here

from random import randrange

numbers = [str(randrange(111, 777)) + '\n' for _ in range(25)]

filename = 'random.txt'

with open(filename, 'w', encoding='utf-8') as file:
    file.writelines(numbers)