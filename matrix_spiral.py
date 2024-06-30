n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

q = 0
r = 0
c = 0
counter = 0
while q < n * m:
    if r == c == n // 2 and (n != 1 and m != 1):  # решает проблему с заполнением последней клетки
        q += 1
        matrix[r][c] = q
        break
    while c < m - 1 - counter and q < n * m:
        q += 1
        matrix[r][c] = q
        c += 1
    while r < n - 1 - counter and q < n * m:
        q += 1
        matrix[r][c] = q
        r += 1
    while c > counter and q < n * m:
        q += 1
        matrix[r][c] = q
        c -= 1
    while r > counter and q < n * m:
        q += 1
        matrix[r][c] = q
        r -= 1
    counter += 1
    r += 1
    c += 1


for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()