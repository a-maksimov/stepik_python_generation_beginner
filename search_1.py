# put your python code here

n = int(input())

strings = []
results = []

for i in range(n):
    strings.append(input())
query = input()

for string in strings:
    if query.lower() in string.lower():
        results.append(string)
print(*results, sep='\n')
