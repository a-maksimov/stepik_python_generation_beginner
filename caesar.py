# put your python code here

n, string = int(input()), input()

shift = ord('a')

for c in string:
    if ord(c) - shift - n >= 0:
        print(chr(ord(c) - n), end='')
    else:
        print(chr(ord('z') - abs((ord(c) - shift - n + 1))), end='')