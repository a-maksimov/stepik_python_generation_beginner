numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
           (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
           (90, 1, -45, -21)]


def comparator(args):
    sum_args = sum(args)
    mean = sum_args / len(args)
    return mean


print(min(numbers, key=comparator))
print(max(numbers, key=comparator))
