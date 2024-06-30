import func_is_prime


# объявление функции
def get_next_prime(num):
    j = 1
    while not func_is_prime.is_prime(num + j):
        j += 1
    return num + j


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
