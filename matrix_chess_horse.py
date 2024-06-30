# put your python code here

board = []
for _ in range(8):
    board.append(['.'] * 8)

square = input()

c = ord(square[0]) - ord('a')
r = 8 - int(square[1])

board[r][c] = 'N'

for row in range(8):
    for col in range(8):
        if abs(r - row) == 1 and abs(c - col) == 2 or abs(r - row) == 2 and abs(c - col) == 1:
            board[row][col] = '*'

for row in range(8):
    print(' '.join(desk[row]))

for row in range(8):
    print(' '.join(board[row]))
#     x, y = input()
#     n = 8
#     board = [['.'] * n for _ in range(n)]
#     x = ord(x) - 97
#     y = n - int(y)
#     board[y][x] = 'N'
#
#     for i in range(n):
#         for j in range(n):
#             if abs(y - i) * abs(x - j) == 2:
#                 board[i][j] = '*'
#
#     for row in board:
#         print(*row)
