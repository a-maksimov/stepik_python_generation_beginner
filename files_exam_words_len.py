with open('words.txt', 'r', encoding='utf-8') as file:
    content = file.read()
words = content.split()
max_len = len(max(words, key=len))
for word in words:
    if len(word) == max_len:
        print(word)
