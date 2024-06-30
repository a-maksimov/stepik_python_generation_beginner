string = input()

ls = string.split()
count = 0

for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[j] == ls[i]:
            count += 1
print(count)
