string = 'ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР'

maximum = 0
for i in range(len(string)):
    if string[i] == 'Р':
        counter = 0
        for j in range(len(string) - i):
            if string[i + j] != 'Р':
                break
            else:
                counter += 1
        if counter > maximum:
            maximum = counter
print(maximum)

# # put your python code here
# s = input().split('О')
# print(len(max(s)))