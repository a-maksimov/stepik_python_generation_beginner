for b in range(101):
    for c in range(101):
        for t in range(101):
            if (10 * b + 5 * c + 0.5 * t == 100) and (b + c + t == 100):
                print('b =', b, 'c =', c, 't =', t)
