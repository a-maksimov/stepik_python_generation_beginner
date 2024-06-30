# put your python code here

from math import gcd
from fractions import Fraction

n = int(input())

for i in range(1, n // 2 + 1):
    j = n - i
    while i < j:
        if i + j == n and gcd(i, j) == 1:
            result = Fraction(i, j)
        j -= 1



print(result)