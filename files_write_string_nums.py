filename = 'input.txt'

with open(filename, 'r', encoding='utf-8') as file:
    input_lines = [line.strip() for line in file.readlines()]

with open('output.txt', 'w', encoding='utf-8') as file:
    output_lines = [str(num + 1) + ') ' + line + '\n' for (num, line) in enumerate(input_lines)]
    file.writelines(output_lines)

# with open('input.txt') as fin, open('output.txt', 'w') as fout:
#     [fout.write(f'{i}) {line}') for i, line in enumerate(fin, 1)]