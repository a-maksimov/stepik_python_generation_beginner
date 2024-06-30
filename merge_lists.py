def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


# считываем данные
n = int(input())

string_lists_nums = []
string_list_nums = []

for _ in range(n):
    string = input()
    string_list = string.split()
    for i in range(len(string_list)):
        string_list_nums.append(int(string_list[i]))
    string_lists_nums.append(string_list_nums)
    string_list_nums = []

merged_list = []
for i in range(n - 1):
    if not merged_list:
        string_list_num_1 = string_lists_nums[i]
    string_list_num_2 = string_lists_nums[i + 1]
    merged_list = quick_merge(string_list_num_1, string_list_num_2)
    string_list_num_1 = merged_list

print(merged_list)