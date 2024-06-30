# put your python code here

n = 2

num_list = [2,
0,
4,
8,
16,
13]

# for i in range(1, n + 1):
#     num = int(input())
#     num_list.append(num)

num = int(num_list[-1])
num_list = num_list[:-1]

result = False
if len(num_list) > 1:
    for i in range(len(num_list)):
        new_num_list = num_list[:i] + num_list[i + 1:]
        for j in range(len(new_num_list)):
            if num == num_list[i] * new_num_list[j]:
                result = True
                break
if result:
    print('ДА')
else:
    print('НЕТ')