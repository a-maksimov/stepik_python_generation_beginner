# put your python code here

n = int(input())

matrix = []

for _ in range(n):
    row = input().split()
    matrix.append(row)

for i in range(n):
    for j in range(n):
        matrix[i][j] = int(matrix[i][j])

# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)

for row in matrix:
    count = 0
    m = sum(row)/len(row)
    for elem in row:
        if elem > m:
            count += 1
    print(count)
