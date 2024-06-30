def merge(values):  # values - это список словарей
    merged = {}
    for dict_item in values:
        for letter in dict_item:
            merged[letter] = merged.setdefault(letter, set())
            merged[letter].add(dict_item[letter])

    return merged


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])

print(result)
