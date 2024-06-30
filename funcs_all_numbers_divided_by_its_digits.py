# put your python code here

a = input()

b = input()


def check_num(num1, num2):
    num_list = list(filter(lambda num: '0' not in str(num), range(int(num1), int(num2) + 1)))
    return list(filter(lambda num: all(map(lambda digit: num % int(digit) == 0, str(num))), num_list))


print(*check_num(a, b))
