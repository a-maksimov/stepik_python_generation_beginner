def print_products(*args):
    products = [arg for arg in args if isinstance(arg, str) and len(arg) > 0]
    if len(products) > 0:
        for i in range(len(products)):
            print(f'{i + 1}) {products[i]}')
    else:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)

print_products([4], {}, 1, 2, {'Beegeek'}, '')

