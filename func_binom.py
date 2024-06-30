# объявление функции
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def compute_binom(n, k):
    binom = factorial(n) / (factorial(k) * factorial(n - k))
    return int(binom)


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
