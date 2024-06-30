# put your python code here

string = '1 2 3 4 5'

num_list = string.split()

num_list = num_list[-1:] + num_list[:-1]

print(*num_list)