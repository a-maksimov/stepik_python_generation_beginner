for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                for e in range(d, 151):
                    if a**5 + b**5 + c**5 + d**5 == e**5:
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
