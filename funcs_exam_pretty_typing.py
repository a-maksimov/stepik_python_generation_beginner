def pretty_print(data, side='-', delimiter='|'):
    from functools import reduce
    data = [str(word) for word in data]
    middle = reduce(lambda word1, word2: word1 + word2 + ' ' + delimiter + ' ', data, delimiter + ' ')
    symlen = len(middle) - 3
    top_and_bottom = ' ' + side * symlen + ' '
    print(top_and_bottom)
    print(middle)
    print(top_and_bottom)

# def pretty_print(data, side='-', delimeter='|'):
#     line = f" {delimeter} ".join(map(str, data))
#     print(' ' + side * (2 + len(line)))
#     print(delimeter + ' ' + line + ' ' + delimeter)
#     print(' ' + side * (2 + len(line)))


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
