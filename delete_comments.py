# put your python code here

strnum = input()
n = int(strnum[1:])

for i in range(n):
    string = input()
    if '#' in string:
        string = string.split('#')
        del string[1]
        string = string[0]
        string = string.rstrip()
    print(string)