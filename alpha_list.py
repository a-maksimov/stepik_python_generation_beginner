# put your python code here

n = int(input())

shift = ord('a')

ls = list(chr(i) for i in range(shift, shift + n))
print(ls)