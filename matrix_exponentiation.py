# put your python code here

def matrix_exp(mat, exp):
    n = len(mat)
    m = len(mat[0])
    matrix = mat
    for _ in range(exp - 1):
        mat_temp = [[0] * m for _ in range(n)]
        for r in range(n):
            for c in range(n):
                for a in range(n):
                    mat_temp[r][c] += matrix[r][a] * mat[a][c]
        matrix = mat_temp
    return matrix


n = int(input())
matrix = []
for i in range(n):
    row = input().split()
    row = [int(elem) for elem in row]
    matrix.append(row)

e = int(input())

matrix = matrix_exp(matrix, e)

for row in range(n):
    print(*matrix[row])