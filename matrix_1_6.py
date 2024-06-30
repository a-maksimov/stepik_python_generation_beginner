# put your python code here

n = int(input())

matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

maximum = matrix[0][0]
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            if matrix[i][j] >= maximum:
                maximum = matrix[i][j]
print(maximum)
