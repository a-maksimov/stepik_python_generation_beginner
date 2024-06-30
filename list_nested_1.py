# put your python code here

n = int(input())
ls = []

my_list = [[1 + i for i in range(n)] for _ in range(n)]

for item in my_list:
    print(item)

# n = int(input())
# print(*[[i for i in range(1, n+1)] for i in range(1, n+1)], sep = "\n")