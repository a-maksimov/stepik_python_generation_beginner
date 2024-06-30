# put your python code here
ls = ['a']
shift = ord('a')

for i in range(1, 26):
    ls.append(chr((shift + i)) * (i + 1))
print(ls)
print(ls[-1])
