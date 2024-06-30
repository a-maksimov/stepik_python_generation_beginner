import random

n = int(input())    # количество попыток

for _ in range(n):
    res = random.randrange(2)
    if res == 0:
        print('Орел')
    else:
        print('Решка')


# from random import randint
#
# COIN = ['Орел', 'Решка']
#
# for _ in range(int(input())):
#     print(COIN[randint(0, 1)])