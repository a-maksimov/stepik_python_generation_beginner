# put your python code here

# n = int(input())
# flag = True
# list = []
# for string_num in range(n):
#     char_in_string = True
#     string = input()
#     for char in 'anton':
#         if char not in string:
#             char_in_string = False
#     if flag and char_in_string:
#         for a in range(len(string)):
#             if string[a] == 'a':
#                 index = a + 1
#                 string = string[index:]
#                 for b in range(len(string)):
#                     if string[b] == 'n':
#                         index = b + 1
#                         string = string[index:]
#                         for c in range(len(string)):
#                             if string[c] == 't':
#                                 index = c + 1
#                                 string = string[index:]
#                                 for d in range(len(string)):
#                                     if string[d] == 'o':
#                                         index = d + 1
#                                         string = string[index:]
#                                         if 'n' in string:
#                                             list.append(string_num + 1)
#                                             break
#                                         else:
#                                             break
#                                 break
#                         break
#                 break
# print(*list)

for i in range(int(input())):
    s, virus, x = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break
