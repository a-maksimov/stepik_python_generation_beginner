# объявление функции
def is_pangram(text):
    shift = ord('a')
    result = True
    for i in range(26):
        char = chr(shift + i)
        if char not in text.lower():
            result = False
            break
    if result:
        return True
    else:
        return False

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))