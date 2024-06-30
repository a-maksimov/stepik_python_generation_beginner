from random import sample

filename1, filename2 = 'first_names.txt', 'last_names.txt'

with open(filename1, 'r', encoding='utf-8') as first_names, open(filename2, 'r', encoding='utf-8') as last_names:
    sample_first_names = [first_name.strip() for first_name in sample(first_names.readlines(), 3)]
    sample_last_names = [last_name.strip() for last_name in sample(last_names.readlines(), 3)]
    [print(*[first_name, last_name]) for first_name, last_name in zip(sample_first_names, sample_last_names)]
