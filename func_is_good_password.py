# объявление функции
def is_password_good(password):
    if len(password) < 8:
        good = False
    elif password.lower() == password or password.upper() == password:
        good = False
    elif password.isalpha():
        good = False
    else:
        good = True
    if good:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))