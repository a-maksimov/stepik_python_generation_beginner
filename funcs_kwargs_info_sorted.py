def info_kwargs(**kwargs):
    keys = sorted(kwargs)
    for key in keys:
        print(f'{key}: {kwargs[key]}')


# def info_kwargs(**kwargs):
#     for k, v in sorted(kwargs.items()):
#         print(f'{k}: {v}')

# def info_kwargs(**kwargs):
#     [print(f'{key}: {kwargs[key]}') for key in sorted(kwargs.keys())]

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
