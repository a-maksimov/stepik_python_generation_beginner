# put your python code here

n, m = [int(i) for i in input().split()]

matrix1 = []

for i in range(n):
    row = input().split()
    row = [int(elem) for elem in row]
    matrix1.append(row)
input()

m, k = [int(i) for i in input().split()]

matrix2 = []

for i in range(m):
    row = input().split()
    row = [int(elem) for elem in row]
    matrix2.append(row)

matrix3 = [[0] * k for row in range(n)]

for r in range(n):
    for c in range(k):
        for a in range(m):
            matrix3[r][c] += matrix1[r][a] * matrix2[a][c]

for row in range(n):
    print(*matrix3[row])