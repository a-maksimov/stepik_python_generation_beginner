# put your python code here

n = int(input())

matrix = [[int(item) for item in input().split()] for _ in range(n)]

for c in range(n):
    for r in range(n - 1, -1, -1):
        print(matrix[r][c], end=' ')
    print()