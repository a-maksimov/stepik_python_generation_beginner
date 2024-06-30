# put your python code here

from random import shuffle as shuffle

n = int(input())

ls = []

for _ in range(n):
    ls.append(input())

ls_shuffle = ls.copy()

shuffle(ls_shuffle)

i = 0
while i < n:
    if ls_shuffle.index(ls[i]) != ls.index(ls[i]):
        i += 1
    else:
        shuffle(ls_shuffle)
        i = 0
        continue

for i in range(n):
    print(f'{ls[i]} - {ls_shuffle[i]}')