def arithmetic_operation(operation):
    add = lambda x, y: x + y
    subt = lambda x, y: x - y
    mult = lambda x, y: x * y
    div = lambda x, y: x / y
    operations = {'+': add, '-': subt, '*': mult, '/': div}
    return operations[operation]


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))

# from operator import *
#
# def arithmetic_operation(operation):
#     oper = {
#         '+': add,
#         '-': sub,
#         '*': mul,
#         '/': truediv
#     }
#     return oper[operation]

# def arithmetic_operation(op):
#     return lambda x, y: eval(f"{x}{op}{y}")
