# объявление функции
def is_palindrome(text):
    text = text.lower()
    text = text.strip()
    text = text.replace(' ', '')
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('-', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    if text == text[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))