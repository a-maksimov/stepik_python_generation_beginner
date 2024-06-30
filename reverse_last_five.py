# put your python code here

num = int(input())

if num > 99999:
    numstr = str(num // 100000)
else:
    numstr = ''

for i in range(5):
    num_last = num % 10
    numstr += str(num_last)
    num //= 10

print(numstr.lstrip('0'))

# s = input()
# print(int(s[:-5] + s[-5:][::-1]))