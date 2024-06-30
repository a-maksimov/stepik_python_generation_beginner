# put your python code here

import random

tickets = set()

while len(tickets) <= 99:
    tickets.add(random.randint(1000000, 9999999))

print(*tickets, sep='\n')
print(len(tickets))
