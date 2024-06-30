filename = 'population.txt'

with open(filename, 'r', encoding='utf-8') as file:
    countries = [country.split('\t') for country in file.readlines()]
    countries_filtered = filter(lambda country: country[0].startswith('G') and int(country[1]) > 500000, countries)
    for country in countries_filtered:
        print(country[0])

