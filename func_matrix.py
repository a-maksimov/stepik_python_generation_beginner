def matrix(n=None, m=None, fill=None):
    if fill is None:
        fill = 0
    if n is None:
        n = 1
    if m is None:
        m = n
    matrix = [[fill] * m for _ in range(n)]
    return matrix

print(matrix())                   # матрица 1 × 1 из 0
print(matrix(3))                  # матрица 3 × 3 из 0
print(matrix(2, 5))               # матрица 2 × 5 из 0
print(matrix(3, 4, 9))            # матрица 3 × 4 из 9