people = list(range(1, n + 1))
# убираем каждый k-й элемент, пока длина списка больше или равна k
while len(people) >= k:
    if len(people) == 1:
        break
    del people[k - 1]
    people = people[k - 1:] + people[:k - 1]
# после того как длина списка стала меньше k, используем остаток от деления, чтобы всегда оставаться внутри списка
while len(people) > 1:
    index = (k - 1) % len(people)
    del people[index]
    people = people[index:] + people[:index]
print(*people)