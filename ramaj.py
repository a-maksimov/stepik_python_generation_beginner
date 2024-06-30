maximum = 0

for _ in range(1, 6):
    for a in range(1, 33):
        for b in range(1, 33):
            for c in range(1, 33):
                for d in range(1, 33):
                    if (a ** 3 + b ** 3 == c ** 3 + d ** 3) and a != b and a != c and a != d and b != c and b != d and c != d:
                        e = a ** 3 + b ** 3
                        print(e)
                        break
