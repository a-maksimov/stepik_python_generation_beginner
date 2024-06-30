# # put your python code here
#
# from random import randrange as r
#
#
# def gen_row():
#     row = set()
#     while len(row) != 5:
#         row.add(r(1, 76))
#     return list(row)
#
#
# bingo = [gen_row()]
#
# while len(bingo) != 5:
#     new_row = gen_row()
#     for row in bingo:
#         for num in new_row:
#             if num not in row:
#                 continue
#             else:
#                 break
#             break
#     bingo.append(new_row)
#
# bingo[2][2] = 0
#
# for r in range(5):
#     for c in range(5):
#         print(str(bingo[r][c]).ljust(3), end='')
#     print()

# put your python code here

from random import sample as sample

ls = list(range(1, 76))
sm = sample(ls, 25)

bingo = [[0] * 5 for _ in range(5)]

for i in range(5):
    bingo[i] = sm[:5]
    sm = sm[5:]

bingo[2][2] = 0

for r in range(5):
    for c in range(5):
        print(str(bingo[r][c]).ljust(3), end='')
    print()

