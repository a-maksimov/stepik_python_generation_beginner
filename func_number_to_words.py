# объявление функции
def number_to_words(num):
    nums = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
            'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать',
            'девятнадцать']
    decimals = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if 1 <= num <= 19:
        result = nums[num - 1]
    else:
        decimal = decimals[num // 10 - 2]
        if num % 10 == 0:
            result = decimal
        else:
            number = nums[num % 10 - 1]
            result = decimal + ' ' + number
    return result


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))