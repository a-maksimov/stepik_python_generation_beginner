# put your python code here

d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

string = input().upper().replace('"', '')

for sym in string:
    for value in d.values():
        if sym in value:
            for key in d:
                if sym in d[key]:
                    for _ in range(d[key].index(sym) + 1):
                        print(key, end='')
                    break
            break

# for letter in input().upper():
#     for key, value in keyboard.items():
#         if letter in value:
#             print(key * (value.index(letter) + 1), end="")