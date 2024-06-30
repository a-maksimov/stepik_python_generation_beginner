# put your python code here

n, m = [int(i) for i in input().split()]
list = list(range(1, n * m + 1))
matrix = []

for row in range(n):
    row = list[:m]
    matrix.append(row)
    list = list[m:]

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()