def concat(*args, sep=' '):
    data = list(map(lambda word: str(word) if isinstance(word, int) else word, args))
    return sep.join(data)

print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))