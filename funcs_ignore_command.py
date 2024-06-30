def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda input_command: input_command in command, ignore))


print(ignore_command('alias'))
print(ignore_command('all'))
print(ignore_command('alias all'))
print(ignore_command('set all'))

