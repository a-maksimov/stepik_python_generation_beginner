x, y = input()
n = 8
board = [['.'] * n for _ in range(n)]
x = ord(x) - 97
y = n - int(y)

for i in range(n):
    for j in range(n):
        if i == y or j == x or x + i == y + j or i - x == y - j:
            board[i][j] = '*'

board[y][x] = 'Q'

for row in board:
    print(*row)