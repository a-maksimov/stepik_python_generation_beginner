a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88]

n = len(a)
indexes = [a.index(num) for num in a]

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    indexes_sorted = [a.index(num) for num in a]
    if indexes_sorted != indexes:
        indexes = indexes_sorted
    else:
        break

print(a)

n = len(a)

# Если при очередной итерации второго for'а не произошло ни одной перестановки, то прерываем работу первого.
# for i in range(n - 1):
#     flag = True
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = False
#     if flag:
#         break
# print(a)