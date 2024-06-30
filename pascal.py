# put your python code here

def pascal(n):
    n += 2
    ls = []
    inlist = [0, 1, 0]
    ls.append(inlist)
    for i in range(2, n + 1):
        inlist = [0] * (i + 2)
        for j in range(len(inlist) - 2):
            inlist_item = ls[i - 2][j] + ls[i - 2][j + 1]
            inlist[j + 1] = inlist_item
        ls.append(inlist)
    row = ls[n - 2]
    return row[1:-1]


num = int(input())
print(pascal(num))

# # -------------------ФУНКЦИЯ-------------------
# def pascal(n):
#     triangle = [[1]]
#
#     for i in range(n):
#         row = [1]
#         for j in range(1, len(triangle[i])):
#             row += [sum(triangle[i][j - 1: j + 1])]
#         row += [1]
#         triangle.append(row.copy())
#
#     return triangle[n]
#
#
# # --------------------ВЫЗОВ--------------------
# print(pascal(int(input())))