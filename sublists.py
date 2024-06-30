# put your python code here
def sublist(sl, n):
    res = []
    i = n - 1
    while len(sl) > i:
        res.append(sl[:n])
        sl = sl[n - i:]
    return res


sublists = [[]]
string_list = input().split()
for i in range(1, len(string_list) + 1):
    result = sublist(string_list, i)
    for elem in result:
        sublists.append(elem)
print(sublists)
