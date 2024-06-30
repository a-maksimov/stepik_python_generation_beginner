# put your python code here

n = input()

numstr = ''
string = ''
for i in range(0, len(n), 3):
    numstr = n[:-3 - i] + ',' +  n[-3 - i:]
    string = numstr[-3 - 1 - i: -i] + string
str = string[1:] + ',' + n[-3:]
str_strip = str.strip(',')
print(str_strip)

# num = input()
# for idx in range(len(num) - 3, 0, -3):
#     num = num[:idx] + ',' + num[idx:]
# print(num)