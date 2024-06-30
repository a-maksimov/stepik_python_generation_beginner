# объявление функции
def draw_triangle():
    for i in range(8):
        print(' ' * (8 - 1 - i) + '*' * (2 * i + 1))

# основная программа
draw_triangle()  # вызов функции