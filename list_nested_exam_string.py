# put your python code here

ls = input().split()

n = int(input())

result = [[] * n for _ in range(n)]

for i in range(n):
    for j in range(0, len(ls), n):
        result[i].append(ls[j])
    ls = ls[1:]
print(result)