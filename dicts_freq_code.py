# put your python code here

string = input()

word = {}

for sym in string:
    word[sym] = word.setdefault(sym, 0) + 1

n = int(input())

dict = {}

for _ in range(n):
    letter, freq = input().split(': ')
    dict[int(freq)] = letter

new_string = ''

for sym in string:
    sym_freq = word.get(sym)
    new_sym = dict[sym_freq]
    new_string = new_string + new_sym

print(new_string)
