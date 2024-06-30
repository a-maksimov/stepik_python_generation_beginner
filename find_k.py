# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.
#
# Формат входных данных На вход программе подается натуральное число n,  далее n строк, каждая на отдельной строке. В
# конце вводится натуральное число k – номер буквы (нумерация начинается с единицы).
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание. Если некоторые строки слишком короткие, и в них нет символа с заданным номером, то такие строки при
# выводе нужно игнорировать.

n = int(input())

ls = []
lengths = []

# создаем сисок со всеми символами и список длин введенных строк
for i in range(n):
    string = input()
    ls.extend(string)
    lengths.append(len(string))

k = int(input())
start = 0

# создаем строки длиной из списка длин, состоящие из символов
# ищем k-символ, если длина строки не менее k
for i in range(n):
    string = ls[start:lengths[i] + start]
    start += lengths[i]
    if len(string) >= k:
        print(string[k - 1], end='')