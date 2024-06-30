# put your python code here

n, m = int(input()), int(input())

matrix = []

for i in range(n):
    row = input().split()
    matrix.append(row)

for i in range(n):
    for j in range(m):
        matrix[i][j] = int(matrix[i][j])

maximum = matrix[0][0]
max_i, max_j = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] > maximum:
            max_i, max_j = i, j
            maximum = matrix[i][j]
print(max_i, max_j)