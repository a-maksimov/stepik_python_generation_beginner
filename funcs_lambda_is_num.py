is_non_negative_num = lambda string: string.replace('.', '', 1).isdigit()

is_num = lambda string: is_non_negative_num(string[1:]) if string[0] == '-' else is_non_negative_num(string)