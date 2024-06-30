# put your python code here

string_list = input().split()

dict = {}
for word in string_list:
    dict[word] = dict.get(word, -1) + 1
    if dict[word] > 0:
        print(word + '_' + str(dict[word]), end=' ')
    else:
        print(word, end=' ')