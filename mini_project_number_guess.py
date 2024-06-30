from random import *

print('Это игра, в которой нужно угадать число в интервале чисел')
print('Введите начало интервала: ', end='')
start = int(input())
print('Введите конец интервала: ', end='')
stop = int(input())

number = randint(start, stop)

print(f'Случайное число в интервале от {start} до {stop} сгенерировано.\nТеперь попробуйте его угадать.\n\
Для этого введите целое число от {start} до {stop}:', end='')
number_guess = int(input())

while number_guess:
    if number_guess > number:
        print('Слишком много, попробуйте еще раз: ', end='')
        number_guess = int(input())
    elif number_guess < number:
        print('Слишком мало, попробуйте еще раз: ', end='')
        number_guess = int(input())
    else:
        break

print('Вы угадали, поздравляем!')