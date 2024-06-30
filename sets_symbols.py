# put your python code here

n = int(input())

string = ''
for _ in range(n):
    string += input().lower()

print(len(set(string)))