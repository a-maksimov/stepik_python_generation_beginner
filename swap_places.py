string = '1 2 3 4 5'

num_list = string.split()

for i in range(1, len(num_list), 2):
    num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
print(*num_list)
