# put your python code here

a, b = 'ящерица', 'Спок'
#
# list1 = ['ножницы', 'бумага']
# list2 = ['камень', 'ножницы']
# list3 = ['бумага', 'камень']
# list4 = ['камень', 'ящерица']
# list5 = ['ящерица', 'Спок']
# list6 = ['Спок', 'ножницы']
# list7 = ['ножницы', 'ящерица']
# list8 = ['ящерица', 'бумага']
# list9 = ['бумага', 'Спок']
# list10 = ['Спок', 'камень']
#
# if a != b:
#     if a in list1 and b in list1:
#         if list1.index(a) < list1.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     elif a in list2 and b in list2:
#         if list2.index(a) < list2.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     elif a in list3 and b in list3:
#         if list3.index(a) < list3.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     elif a in list4 and b in list4:
#         if list4.index(a) < list4.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     elif a in list5 and b in list5:
#         if list5.index(a) < list5.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     elif a in list6 and b in list6:
#         if list6.index(a) < list6.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     elif a in list7 and b in list7:
#         if list7.index(a) < list7.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     elif a in list8 and b in list8:
#         if list8.index(a) < list8.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     elif a in list9 and b in list9:
#         if list9.index(a) < list9.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
#     else:
#         if list10.index(a) < list10.index(b):
#             print('Тимур')
#         else:
#             print('Руслан')
# else:
#     print('ничья')

g = ('ножницы', 'бумага', 'камень', 'ящерица', 'Спок')
dist = (g.index(a) - g.index(b)) % len(g)
print(('ничья', 'Тимур', 'Руслан')[dist and dist % 2 + 1])