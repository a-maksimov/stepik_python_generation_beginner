n = int(input())

matrix = []

for i in range(n):
    row = input().split()
    matrix.append(row)

for r in range(n // 2):
    matrix[r], matrix[-r - 1] = matrix[-r - 1], matrix[r]

for r in range(n):
    print(*matrix[r])


# Верное решение #433332609
# Python 3
# n = int(input())
#
# matrix = [[int(item) for item in input().split()] for _ in range(n)]
# matrix.reverse()
#
# for row in matrix:
#     print(*row)