# put your python code here

n = int(input())
strings = []

for i in range(n):
    strings.append(input())

k = int(input())
queries = []

for i in range(k):
    queries.append(input())

results = []

for string in strings:
    result = True
    for query in queries:
        if query.lower() in string.lower():
            new_result = True
        else:
            new_result = False
            break
    result = result and new_result
    if result:
        results.append(string)
print(*results, sep='\n')
