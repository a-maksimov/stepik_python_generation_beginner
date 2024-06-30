numbers = [8, 9, 10, 11]

del numbers[1]
numbers.insert(1, 17)
for i in range(4, 7):
    numbers.append(i)
del numbers[0]
numbers_copy = numbers.copy()
for c in numbers_copy:
    numbers.append(c)
numbers.insert(3, 25)
print(numbers)

# Верное решение #185167901
# Python 3
# numbers = [8, 9, 10, 11]
#
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)
