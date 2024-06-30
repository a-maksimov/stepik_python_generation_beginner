# put your python code here
n, m = input().split()

desk = []
for _ in range(int(n)):
    desk.append(['.'] * int(m))

for row in range(0, int(n), 2):
    for col in range(1, int(m), 2):
        desk[row][col] = '*'

for row in range(1, int(n), 2):
    for col in range(0, int(m), 2):
        desk[row][col] = '*'

for row in range(int(n)):
    print(' '.join(desk[row]))


# n, m = [int(i) for i in input().split()]
# board = [['.'] * m for _ in range(n)]
#
# for i in range(n):
#     for j in range(1 - i % 2, m, 2):
#         board[i][j] = '*'
#
# for row in board:
#     print(*row)