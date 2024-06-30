is_non_negative_num = lambda string: True if set(string).issubset('.0123456789') and string.count('.') <= 1 else False
