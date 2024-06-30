# объявление функции
def find_all(target, symbol):
    indexes = [i for i in range(len(target)) if target[i] == symbol]
    # indexes = []
    # for i in range(len(target)):
    #     if target[i] == symbol:
    #         indexes.append(i)
    return indexes


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
