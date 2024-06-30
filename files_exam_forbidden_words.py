with open('forbidden_words.txt', 'r', encoding='utf-8') as file:
    forbidden_words = file.read().split()

with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    content_lower = content.lower()
for word in forbidden_words:
    if word in content_lower:
        content_lower = content_lower.replace(word, '*' * len(word))
new_content = ''
for sym1, sym2 in zip(content, content_lower):
    if sym2 != '*':
        new_content += sym1
    else:
        new_content += '*'
print(new_content)
