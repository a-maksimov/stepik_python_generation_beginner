# put your python code here


string = input().lower()

sym = ['.', ',', ';', ':', '-', '?', '!']

for i in range(len(sym)):
    while sym[i] in string:
        string = string.replace(sym[i], '')

print(len(set(string.split())))

