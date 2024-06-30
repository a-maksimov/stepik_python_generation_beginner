# put your python code here

a, b = int(input()), int(input())

sum = 0
num = 0

for i in range(a, b + 1):
    last_sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            last_sum = last_sum + j
    if last_sum >= sum:
        sum = last_sum
        if i > num:
            num = i
print(num, sum)