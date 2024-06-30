# put your python code here

string = input()

ls = string.split()

for i in range(len(ls)):
    ls[i] = int(ls[i])

maximum = max(ls)
minimum = min(ls)

max_pos = ls.index(maximum)
min_pos = ls.index(minimum)

ls[max_pos] = minimum
ls[min_pos] = maximum

print(*ls)
