# put your python code here
def chunked(string, n):
    res = []
    ls = string.split()
    while len(ls) >= 1:
        res.append(ls[:n])
        ls = ls[n:]
    return res


print(chunked('a b c d e f', 2))
