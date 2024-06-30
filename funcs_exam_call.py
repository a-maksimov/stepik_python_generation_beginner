def add3(x, y, z):
    return x + y + z


def call(function, *args):
    return function(*args)


print(call(add3, 10, 30, 40))
