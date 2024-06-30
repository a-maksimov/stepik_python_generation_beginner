# put your python code here

string = input()

nums = [int(num) for num in string.split()]


def sum_num(num):
    return sum([int(dig) for dig in str(num)])


print(*sorted(sorted(nums), key=sum_num))
