# put your python code here

string = '1 2 3 4 5'

num_list = string.split()

counter = 0

for i in range(1, len(num_list)):
    if int(num_list[i]) > int(num_list[i - 1]):
        counter += 1
