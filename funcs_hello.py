def greet(name, *args):
    string = f'Hello, {name}!'
    for arg in args:
        string = string[:-1] + f' and {arg}!'
    return string


print(greet('Timur', 'Roman', 'Ruslan'))