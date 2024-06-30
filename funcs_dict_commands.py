# put your python code here

from math import sin

n, command = int(input()), input()


def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def modul(num):
    return abs(num)


def root(num):
    return num ** (1 / 2)


def sine(num):
    return sin(num)


commands = {'квадрат': square(n), 'куб': cube(n), 'корень': root(n), 'модуль': modul(n), 'синус': sine(n)}

print(commands[command])
