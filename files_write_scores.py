with open('class_scores.txt', 'r', encoding='utf-8') as scores_file, \
        open('new_scores.txt', 'w', encoding='utf-8') as new_scores_file:
    old_scores = [line.split() for line in scores_file.readlines()]
    names = [line[0] for line in old_scores]
    marks = [int(line[1]) for line in old_scores]
    new_marks = list(map(lambda mark: mark + 5 if 100 - mark >= 5 else 100, marks))
    new_scores = [f'{name} {str(mark)}\n' for name, mark in zip(names, new_marks)]
    new_scores_file.writelines(new_scores)


# with open('class_scores.txt') as class_scores, open('new_scores.txt', 'w') as new_scores:
#     for line in class_scores:
#         name, score = line.split()
#         score = int(score) + 5
#         if score > 100:
#             score = 100
#         print(name, score, file=new_scores)