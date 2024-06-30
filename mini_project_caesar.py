def code_caesar(language, text, n):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    text_coded = ''
    if language == 1:
        for c in text:
            if c in rus_lower_alphabet:
                char_ord = rus_lower_alphabet.find(c)
                if char_ord + n < len(rus_lower_alphabet):
                    text_coded += rus_lower_alphabet[char_ord + n]
                else:
                    text_coded += rus_lower_alphabet[char_ord + n - len(rus_lower_alphabet)]
            elif c in rus_lower_alphabet:
                char_ord = rus_upper_alphabet.find(c)
                if char_ord + n < len(rus_upper_alphabet):
                    text_coded += rus_upper_alphabet[char_ord + n]
                else:
                    text_coded += rus_upper_alphabet[char_ord + n - len(rus_lower_alphabet)]
            else:
                text_coded += c
    else:
        for c in text:
            if c in eng_lower_alphabet:
                char_ord = eng_lower_alphabet.find(c)
                if char_ord + n < len(eng_lower_alphabet):
                    text_coded += eng_lower_alphabet[char_ord + n]
                else:
                    text_coded += eng_lower_alphabet[char_ord + n - len(eng_lower_alphabet)]
            elif c in eng_upper_alphabet:
                char_ord = eng_upper_alphabet.find(c)
                if char_ord + n < len(eng_upper_alphabet):
                    text_coded += eng_upper_alphabet[char_ord + n]
                else:
                    text_coded += eng_upper_alphabet[char_ord + n - len(eng_lower_alphabet)]
            else:
                text_coded += c
    return text_coded


def decode_caesar(language, text, n):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    texts_decoded = []
    text_decoded = ''
    if language == 1:
        for c in text:
            if c in rus_lower_alphabet:
                char_ord = rus_lower_alphabet.find(c)
                if char_ord - n >= 0:
                    text_decoded += rus_lower_alphabet[char_ord - n]
                else:
                    text_decoded += rus_lower_alphabet[char_ord - n + len(rus_lower_alphabet)]
            elif c in rus_upper_alphabet:
                char_ord = rus_upper_alphabet.find(c)
                if char_ord - n >= 0:
                    text_decoded += rus_upper_alphabet[char_ord - n]
                else:
                    text_decoded += rus_upper_alphabet[char_ord - n + len(rus_upper_alphabet)]
            else:
                text_decoded += c
    else:
        for c in text:
            if c in eng_lower_alphabet:
                char_ord = eng_lower_alphabet.find(c)
                if char_ord - n >= 0:
                    text_decoded += eng_lower_alphabet[char_ord - n]
                else:
                    text_decoded += eng_lower_alphabet[char_ord - n + len(eng_lower_alphabet)]
            elif c in eng_upper_alphabet:
                char_ord = eng_upper_alphabet.find(c)
                if char_ord - n >= 0:
                    text_decoded += eng_upper_alphabet[char_ord - n]
                else:
                    text_decoded += eng_upper_alphabet[char_ord - n + len(eng_upper_alphabet)]
            else:
                text_decoded += c
    return text_decoded

print('Эта программа шифрует и дешифрует шифр Цезаря.')
mode = input('Введите "1", если хотите зашифровать текст. Введите "2", если хотите расшифровать текст.\n')
while not mode.isdigit() or not 1 <= int(mode) <= 2:
    mode = input('Введите "1", если хотите зашифровать текст. Введите "2", если хотите расшифровать текст.\n')

lang = input('Введите "1", если язык текста русский. Введите "2", если язык текста английский.\n')
while not lang.isdigit() or not 1 <= int(lang) <= 2:
    lang = input('Введите "1", если язык текста русский. Введите "2", если язык текста английский.\n')

if int(lang) == 1:
    txt = input('Введите текст на русском языке.\n')
else:
    txt = input('Введите текст на английском языке.\n')

if int(mode) == 1:
    n = input('Введите сдвиг вправо.\n')
    text_coded = code_caesar(int(lang), txt, int(n))
    print(text_coded)
else:
    n = input('Введите интервал сдвигов.\n')
    for i in range(int(n)):
        text_decoded = decode_caesar(int(lang), txt, i)
        print(text_decoded)