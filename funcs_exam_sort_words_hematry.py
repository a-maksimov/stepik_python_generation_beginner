# put your python code here

from functools import reduce

n = int(input())

words = sorted([input() for _ in range(n)])

words_sorted = sorted(words, key=lambda word: reduce(lambda sym1, sym2: sym1 + ord(sym2) - ord('A'), word.upper(), 0))
print(words_sorted)

print(*words_sorted, sep='\n')