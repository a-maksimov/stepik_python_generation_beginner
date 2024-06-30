# put your python code here

n = int(input())
div = 1
num = ''
while div > 0:
    div = n // 2
    res = n % 2
    n = div
    num += str(res)
for c in range(len(num) - 1, -1, -1):
    print(num[c], end='')
