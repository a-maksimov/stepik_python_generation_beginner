# put your python code here

word = 'роскомнадзор'

b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

string = word + ' запретил букву ' + b[0]
print(string)
string = word + ' запретил букву '
print_string_old = ''
for i in range(len(b)):
    index = 0
    while index > -1:
        index = string.find(b[i])
        if index > -1:
            string = string[:index] + string[index + 1:]
    for j in range(1, len(b[i:])):
        if b[j + i] in string:
            print_string = string + b[j + i]
            if print_string != print_string_old:
                print_string_old = print_string
                print_string = print_string.split()
                print(' '.join(print_string))
            break

# word = input() + ' запретил букву'
# for i in range(1072, 1104):
#     if chr(i) in word:
#         print(word + ' ' + chr(i))
#         word = ' '.join(word.replace(chr(i), '').split())