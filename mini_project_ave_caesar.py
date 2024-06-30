def ave_caesar(text):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = [',', '.', '!', '"']
    text_coded_list = []
    text = text.split()
    word_coded = ''
    for word in text:
        word_original = word
        for symbol in symbols:
            word_stripped = word.strip(symbol)
            word = word_stripped
        len_word = len(word)
        for c in word_original:
            if c in eng_lower_alphabet:
                char_ord = eng_lower_alphabet.find(c)
                if char_ord + len_word < len(eng_lower_alphabet):
                    word_coded += eng_lower_alphabet[char_ord + len_word]
                else:
                    word_coded += eng_lower_alphabet[char_ord + len_word - len(eng_lower_alphabet)]
            elif c in eng_upper_alphabet:
                char_ord = eng_upper_alphabet.find(c)
                if char_ord + len_word < len(eng_upper_alphabet):
                    word_coded += eng_upper_alphabet[char_ord + len_word]
                else:
                    word_coded += eng_upper_alphabet[char_ord + len_word - len(eng_lower_alphabet)]
            else:
                word_coded += c
        text_coded_list.append(word_coded)
        word_coded = ''
    text_coded = ' '.join(text_coded_list)
    return text_coded

print('Эта программа шифрует каждое слово строки с помощью шифра Цезаря (циклического сдвига на длину этого слова).')

txt = input('Введите текст на английском языке.\n')

text_coded = ave_caesar(txt)
print(text_coded)
