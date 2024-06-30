from functools import reduce

abscissas = input().split()
ordinates = input().split()
applicates = input().split()


def check_sphere(absc, ordin, applic, radius=2):
    return all(list(map(lambda coordinate: reduce(lambda x, y: float(x) + float(y) ** 2, coordinate) <= radius ** 2,
                        list(zip(absc, ordin, applic)))))


# check_sphere = lambda absc, ordin, applic, radius=2: all(list(
#     map(lambda coordinate: reduce(lambda x, y: float(x) + float(y) ** 2, coordinate) <= radius ** 2,
#         list(zip(absc, ordin, applic)))))

print(check_sphere(abscissas, ordinates, applicates))

# abscissas, ordinates, applicates = (map(float, input().split()) for _ in range(3))
# print(all(map(lambda x, y, z: (x**2+y**2+z**2)**0.5 <=2, abscissas,ordinates,applicates)))
# print(all(x**2 + y**2 + z**2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))
