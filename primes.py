# put your python code here

a, b = int(input()), int(input())
prime = False

for i in range(a, b + 1):
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
        else:
            prime = True
    if prime is True:
        print(i)
