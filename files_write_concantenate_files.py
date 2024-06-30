# put your python code here

n = int(input())

filenames = [input() for _ in range(n)]

with open('output.txt', 'a', encoding='utf-8') as output_file:
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as input_file:
            output_file.write(input_file.read())