# put your python code here

filename = 'output.txt'
string = input()

with open(filename, 'w', encoding='utf-8') as file:
    file.write(string)