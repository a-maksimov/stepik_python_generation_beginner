n = int(input())

nums = [i for i in range(1, n ** 2 + 1)]

matrix = [[int(item) for item in input().split()] for _ in range(n)]

sum_row = sum(matrix[0])
sum_diag_1 = 0
sum_diag_2 = 0
res = True
res_row = True
res_col = True
res_diag = True
res_nums = True

for num in nums:
    res_nums_1 = False
    res_nums_2 = True
    for row in matrix:
        if num in row:
            res_nums_1 = True
        else:
            res_nums_2 = False
    res_nums = res_nums_1 or res_nums_2
    if not res_nums:
        res = False
        break

if res_nums:
    for row in matrix:
        if sum(row) != sum_row:
            res_row = False

    for c in range(n):
        sum_col = 0
        for r in range(n):
            if c == r:
                sum_diag_1 += matrix[c][r]
            if r == n - c - 1:
                sum_diag_2 += matrix[c][r]
            sum_col += matrix[r][c]
        if sum_col != sum(matrix[0]):
            res_col = False

    if sum_diag_1 != sum_row or sum_diag_2 != sum_row:
        res_diag = False

    res = res_row and res_col and res_diag
else:
    res = False

if res:
    print('YES')
else:
    print('NO')

# check = []
# for i in range(cols):  # заполняем проверочный список всеми элементами матрицы
#         check += matrix[i]
#
#     for i in range(1, len(check) + 1):  # проверяем проверочный список на наличие всех чисел в промежутке от 1 до n ** 2
#         if i not in check:
#             return print("NO")  # если нет какого-то числа, то значит дальше нет смысла проверять равенство, завершаем с NO