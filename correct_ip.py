# put your python code here

ip = input()
correct = True

for num in ip.split('.'):
    if 0 <= int(num) <= 255:
        new_correct = True
    else:
        new_correct = False
        break
correct = correct and new_correct
if correct:
    print('ДА')
else:
    print('НЕТ')