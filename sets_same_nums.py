# put your python code here

n = int(input())

myset = set(input())
for _ in range(n - 1):
    myset &= set(input())

print(*sorted(myset))