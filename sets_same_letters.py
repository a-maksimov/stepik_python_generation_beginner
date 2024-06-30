# put your python code here

string_list = input().split()

for i in range(len(string_list) - 1):
    if sorted(set(string_list[i + 1])) == sorted(set(string_list[i])):
        same = 'YES'
    else:
        same = 'NO'
        break
print(same)