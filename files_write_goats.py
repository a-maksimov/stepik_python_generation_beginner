with open('goats.txt', 'r', encoding='utf-8') as goats_file, \
        open('answer.txt', 'w', encoding='utf-8') as answer_file:
    goats_file.readline().strip()
    line = goats_file.readline().strip()
    colours = []
    while line != 'GOATS':
        colours.append(line.split()[0])
        line = goats_file.readline().strip()

    goats = goats_file.read()
    goats_dict = {}
    for colour in colours:
        goats_dict[colour] = goats.count(colour)

    goats_sum = sum(goats_dict.values())

    for colour in goats_dict:
        if (100 * goats_dict[colour]) > 7 * goats_sum:  # избегайте операций деления в выражениях сравнения и
            # домножайте правую и левую часть на делитель.
            print(f'{colour} goat', file=answer_file)





    # names = [line[0] for line in old_scores]
    # marks = [int(line[1]) for line in old_scores]
    # new_marks = list(map(lambda mark: mark + 5 if 100 - mark >= 5 else 100, marks))
    # new_scores = [f'{name} {str(mark)}\n' for name, mark in zip(names, new_marks)]
    # new_scores_file.writelines(new_scores)\