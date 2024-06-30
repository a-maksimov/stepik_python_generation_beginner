filename = 'prices.txt'

file = open(filename, encoding='utf-8')

prices = [int(product.split('\t')[2]) * int(product.split('\t')[1]) for product in file.readlines()]

print(sum(prices))

file.close()

# file = open('prices.txt')
# lines = map(str.split, file)
# print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
# file.close()