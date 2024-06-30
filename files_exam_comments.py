# читаем по одной строке, чтобы не перегрузить память, храним значение предыдущей строки...
# with open(input()) as f:
#     prev, without_comments = ' ', []
#     for line in f:
#         if line.startswith('def') and not prev.startswith('#'):
#             without_comments.append(line[line.find(' ') + 1: line.find('(')])
#         prev = line
#     print('\n'.join(without_comments) if without_comments else 'Best Programming Team')
#
# with open('program.txt', 'r', encoding='utf-8') as file:
#     lines = [line.strip() for line in file]

uncommented = []
if 'def ' in lines[0]:
    uncommented.append(lines[0])
for i in range(1, len(lines)):
    if 'def ' in lines[i]:
        if '#' not in lines[i - 1]:
            uncommented.append(lines[i])

uncommented = list(map(lambda func_def: func_def.split()[1].split('(')[0], uncommented))

if not uncommented:
    print ('Best Programming Team')
else:
    print(*uncommented, sep='\n')

# with open(input(), encoding='utf-8') as inf:
# 	not_commented_funcs, preline = [], ''
# 	for line in inf:
# 		if not preline.startswith('#') and line.startswith('def '):
# 			not_commented_funcs.append(line[4:line.find('(')])
# 		preline = line
# 	print('\n'.join(not_commented_funcs) if not_commented_funcs else 'Best Programming Team')