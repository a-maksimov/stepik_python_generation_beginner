# put your python code here

string = input().split()

st = set()
length = len(st)

for num in string:
    st.add(num.lstrip('0'))
    if len(st) == length:
        print('YES')
    else:
        print('NO')
        length = len(st)