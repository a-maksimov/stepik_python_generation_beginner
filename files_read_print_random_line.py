from random import choice

filename = 'lines.txt'

file = open(filename, encoding='utf-8')

random_line = choice(file.readlines())  # can read just once

print(random_line.strip())

file.close()
