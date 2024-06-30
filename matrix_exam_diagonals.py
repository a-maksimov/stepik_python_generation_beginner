# put your python code here

n = int(input())

matrix = [[0] * n for _ in range(n)]

ls = list(range(n))
ls_temp = ls

for i in range(n):
    matrix[i] = ls_temp
    ls_slice = ls[:i + 2]
    ls_temp = ls_slice[::-1] + ls[1:len(ls) - i - 1]

for row in range(n):
    print(*matrix[row])
