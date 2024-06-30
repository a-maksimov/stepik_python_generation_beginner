# put your python code here

n, m = [int(i) for i in input().split()]

matrix1 = []
matrix2 = []

for i in range(n):
    row = input().split()
    row = [int(elem) for elem in row]
    matrix1.append(row)
input()
for i in range(n):
    row = input().split()
    row = [int(elem) for elem in row]
    matrix2.append(row)

for r in range(n):
    for c in range(m):
        matrix2[r][c] = matrix1[r][c] + matrix2[r][c]

for row in range(n):
    print(*matrix2[row])