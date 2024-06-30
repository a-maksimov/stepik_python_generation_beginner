# put your python code here

n = int(input())

matrix = []

for i in range(n):
    row = input().split()
    matrix.append(row)

sum = 0
for i in range(n):
    sum += int(matrix[i][i])

print(sum)