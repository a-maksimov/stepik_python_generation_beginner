with open('logfile.txt', 'r', encoding='utf-8') as logfile, open('output.txt', 'w', encoding='utf-8') as output_file:
    log = [line.split(', ') for line in logfile]
    log_dict = {item[0]: (item[1], item[2].strip()) for item in log}

    for item in log_dict:
        time_enter, time_exit = log_dict[item]
        time_enter_minutes = int(time_enter.split(':')[0]) * 60 + int(time_enter.split(':')[1])
        time_exit_minutes = int(time_exit.split(':')[0]) * 60 + int(time_exit.split(':')[1])
        if time_exit_minutes - time_enter_minutes >= 60:
            print(item, file=output_file)

# def get_diff_mins(time2, time1):
#     t2 = list(map(int, time2.split(':')))
#     t1 = list(map(int, time1.split(':')))
#     return (t2[0]*60 + t2[1]) - (t1[0]*60 + t1[1])
#
# with open('logfile.txt', encoding='utf-8') as inputf, open('output.txt', 'w') as outputf:
#     for fn in inputf:
#         name, time1, time2 = fn.strip().split(', ')
#         if get_diff_mins(time2, time1) >= 60:
#             print(name, file=outputf)

with open('ledger.txt', 'r', encoding='utf-8') as file:
    print(f'$ {sum([int(line.strip("$")) for line in file.readlines()])}')
