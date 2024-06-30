# put your python code here

string = input()
maximum = 0
max_sym = ''

for c in range(len(string)):
    string_replaced = string.replace(string[c], '*')
    count = 0
    for i in range(len(string)):
        if string[i] != string_replaced[i]:
            count += 1
    if count >= maximum:
        maximum = count
        max_sym = string[c]
print(max_sym)