# put your python code here

string = 'w w w o r l d g g w w'

ls = string.split()
string_length = len(ls)
res_list = []
counter = 0
while ls:
    if len(ls) == 1:
        if res_list[-1][-1] == ls[0]:
            res_list[-1].append(ls[0])
        else:
            res_list.append([ls[0]])
        break
    else:
        nlist = []
        i = 0
        nlist.append(ls[i])
        while ls[i + 1] == ls[i]:
            nlist.append(ls[i + 1])
            i += 1
            counter += 1
            if counter == string_length - 1:
                break
        res_list.append(nlist)
        ls = ls[i + 1:]
        counter += 1
print(res_list)

# res = []
#
# for el in input().split():
#     if res and el in res[-1]:
#         res[-1].append(el)
#     else:
#         res.append([el])
#
# print(res)


# a, s, x = input().split(), [], ''
# for i in a:
#     if x != i:
#         s.append(list(i))
#     else:
#         s[-1].append(i)
#     x = i
# print(s)