def sq_sum(*args):
    if len(args) == 0:
        sum = 0
    else:
        sum = args[0]**2
        for i in range(1, len(args)):
            sq = args[i]**2
            sum += sq
    return sum

print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))