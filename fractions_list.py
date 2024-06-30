# put your python code here

n = int(input())

from fractions import Fraction

fractions = sorted(list({Fraction(j, k) for j in range(1, n) for k in range(2, n + 1) if j != k and j < k}))

print(*fractions, sep='\n')


