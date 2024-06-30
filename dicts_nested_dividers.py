numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {num: [i for i in range(1, num + 1) if num % i == 0] for num in numbers}

# result = {n: [i for i in range(1, n // 2 + 1) if n % i == 0] + [n] for n in numbers}
