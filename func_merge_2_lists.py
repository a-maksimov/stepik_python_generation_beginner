# объявление функции
def merge(list1, list2):
    list1.extend(list2)
    for i in range(1, len(list1)):
        elem = list1[i]  # первый элемент из неотсортированной части списка
        j = i
        while j >= 1 and list1[j - 1] > elem:
            list1[j] = list1[j - 1]
            j -= 1
        list1[j] = elem
    return list1

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))