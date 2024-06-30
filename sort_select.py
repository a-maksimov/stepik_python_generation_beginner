a = [78, -32, 5, 39, 58, -5, -63, 57]

n = len(a)

# реализация алгоритма сортировки выбором
for i in range(n):
    ls = a[:n - i]
    maximum = max(ls)
    index = ls.index(maximum)
    del ls[index]
    ls.extend([maximum])
    a[:n - i] = ls.copy()

print(a)
