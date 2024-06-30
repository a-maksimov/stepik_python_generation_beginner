# put your python code here

m, n = int(input()), int(input())

math = set()
cs = set()

for _ in range(m + n):
    prev_math = len(math)
    student = input()
    math.add(student)
    if len(math) == prev_math:
        cs.add(student)

if len(math - cs) + len(cs - math):
    print(len(math - cs) + len(cs - math))
else:
    print('NO')