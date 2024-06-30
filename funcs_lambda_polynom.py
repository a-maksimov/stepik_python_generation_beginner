# put your python code here

from functools import reduce
from operator import add


def evaluate(coefficients, x):
    coefficients.reverse()
    poly_list = list(map(lambda i: int(coefficients[i]) * int(x) ** i, range(len(coefficients) - 1, -1, -1)))
    polynom = reduce(add, poly_list)
    return polynom


print(evaluate(input().split(), input()))

# воспользуемся разложением многочлена по схеме Горнера:
# evaluate = lambda coefficients, x: reduce(lambda s, a: s * x + a, coefficients, 0)
#
# print(evaluate([*map(int, input().split())], int(input())))