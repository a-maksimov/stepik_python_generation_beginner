# put your python code here

n = int(input())
ls = []

for i in range(n):
    inlist = []
    for j in range(i + 1):
        inlist.append(j + 1)
    ls.append(inlist)

print(*ls, sep='\n')