# put your python code here

str = input()
counter = 0
last_char = ''

for c in range(len(str)):
    if last_char == str[c]:
        continue
    for i in range(1, len(str) - c):
        if str[c] == str[c + i]:
            counter += 1
            last_char = str[c]
print(counter)