# объявление функции
def is_prime(num):
    prime = True
    if num == 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0 and i != num:
                prime = False
                break
            else:
                prime = True
    if prime is True:
        return True
    else:
        return False

# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))