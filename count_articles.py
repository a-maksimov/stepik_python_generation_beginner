# put your python code here

string = input()
string_lower = string.lower()
string_list = string_lower.split()

articles = ['a', 'an', 'the']

count = 0

for article in articles:
    count_article = string_list.count(article)
    count += count_article
print('Общее количество артиклей: {}'.format(count))