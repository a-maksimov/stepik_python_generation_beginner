# объявление функции
def is_magic(date):
    date_list = date.split('.')
    day = int(date_list[0].strip())
    month = int(date_list[1].strip())
    year = int(date_list[2]) % 100
    if day * month == year:
        return True
    else:
        return False


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))