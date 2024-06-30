# объявление функции
def convert_to_python_case(text):
    text_list = []
    j = 0
    for i in range(1, len(text)):
        if text[i] != text[i].lower() or i == len(text) - 1:
            text_list.append(text[j:i])
            j = i
    text_list[len(text_list) - 1] = text_list[len(text_list) - 1] + text[-1]  # дописываем последнюю букву к последнему элементу списка
    string = '_'.join(text_list)
    return string.lower()

# считываем данные
txt = input()


# def convert_to_python_case(text):
#     s = ''
#     for el in text:
#         if el.isupper():
#             s += '_'
#         s += el.lower()
#     return s[1:]
#
#
# print(convert_to_python_case(input()))

# вызываем функцию
print(convert_to_python_case(txt))