vol = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

num = int(input())
base = int(input())

s = ''

while num != 0:
    res = num % base
    num //= base
    s = str(vol[res]) + s
print(s)