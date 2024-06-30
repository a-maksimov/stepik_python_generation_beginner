# объявление функции
def is_correct_bracket(text):
    if text[0] == ')':
        result = False
    else:
        count = 0
        for c in text:
            if c == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                break
        if count == 0:
            result = True
        else:
            result = False
    if result:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

# Верное решение #199494042
# Python 3
# # объявление функции
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return not text
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))