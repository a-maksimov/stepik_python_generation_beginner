# put your python code here

string = input()

nums = string.split()


def sum_num(num):
    return sum([int(dig) for dig in num])


print(*sorted(nums, key=sum_num))
