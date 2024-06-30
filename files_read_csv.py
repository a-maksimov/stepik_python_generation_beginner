def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        keys = [key.strip() for key in file.readline().split(',')]
        csv_list = []
        for line in file:
            row = {}
            for key, value in zip(keys, line.split(',')):
                row[key] = value.strip()
            csv_list.append(row)
        return csv_list


# def read_csv():
#     with open('data.csv') as file:
#         keys = file.readline().strip().split(',')
#         return [dict(zip(keys, line.strip().split(','))) for line in file]


filename = 'data.csv'

print(read_csv(filename))
