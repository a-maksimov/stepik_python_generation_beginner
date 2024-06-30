# put your python code here

n = int(input())  # number of classes

marks = []

for _ in range(n):
    clas = {}
    for _ in range(int(input())):
        student, mark = input().split()
        clas[student] = mark
    marks.append(clas)

if all(map(lambda clas: any(map(lambda student: clas[student] == '5', clas)), marks)):
    print('YES')
else:
    print('NO')
