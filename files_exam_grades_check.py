with open('grades.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file.readlines()]
    grades = [map(int, line.split()[1:]) for line in lines]
    count = 0
    for grade in grades:
        check_pass = map(lambda x: x >= 65, grade)
        if all(check_pass):
            count += 1
    print(count)
