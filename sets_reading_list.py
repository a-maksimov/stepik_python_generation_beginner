# put your python code here

m, n = int(input()), int(input())

bib = {input() for _ in range(m)}
bib_length = len(bib)

for _ in range(n):
    bib.add(input())
    if len(bib) == bib_length:
        print('YES')
    else:
        print('NO')
        bib_length = len(bib)




