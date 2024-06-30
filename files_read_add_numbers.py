filename = 'nums.txt'

file = open(filename, encoding='utf-8')

numbers = [int(num.strip()) for num in file.readlines() if num.strip().isdigit()]

print(sum(numbers))

file.close()