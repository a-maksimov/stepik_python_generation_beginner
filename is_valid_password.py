# объявление функций
def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


def is_prime(num):
    prime = True
    if num == 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0 and i != num:
                prime = False
                break
            else:
                prime = True
    if prime is True:
        return True
    else:
        return False


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_valid_password(password):
    password_list = [int(i) for i in password.split(':')]
    if len(password_list) == 3 and (is_palindrome(password_list[0]) and is_prime(password_list[1]) and is_even(password_list[2])):
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
