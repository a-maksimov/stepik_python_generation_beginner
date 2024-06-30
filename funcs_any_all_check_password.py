# put your python code here

string = input()


def check_password(password):
    import string
    return all([
        any(map(lambda sym: sym in string.ascii_lowercase, password)),
        any(map(lambda sym: sym in string.ascii_uppercase, password)),
        any(map(lambda sym: sym in string.digits, password)),
        len(password) >= 7])


if check_password(string):
    print('YES')
else:
    print('NO')

# s = input()
# print('YES' if all((any(i.isupper() for i in s),
#                     any(i.islower() for i in s),
#                     any(i.isdigit() for i in s),
#                     len(s) >= 7)) else 'NO')
