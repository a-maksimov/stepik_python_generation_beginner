# put your python code here

n = int(input())


def ip_dec(ip):
    ip_list = [int(oct) for oct in ip.split('.')]
    ip_list.reverse()
    ip_dec = list(map(lambda i, oct: oct * (256 ** i), range(len(ip_list)), ip_list))
    return sum(ip_dec)


print(*sorted([input() for _ in range(n)], key=lambda ip: ip_dec(ip)), sep='\n')
