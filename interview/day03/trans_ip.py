import sys


def check_ip(ip):
    ip_l = ip.split('.')
    if len(ip_l) != 4:
        return False
    for i in ip_l:
        if not i.isdigit():
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True


def bin_to_int(s):
    n = 0
    for i in range(len(s)):
        if s[i] == '1':
            n |= 1
        if i < len(s) - 1:
            n = n << 1
    return n


def int_to_bin(n):
    s = ''
    while n > 0:
        if n & 1 == 0:
            s = '0' + s
        else:
            s = '1' + s
        n = n >> 1
    return s


def ip_to_int(ip):
    ip_l = list(map(int, ip.split('.')))
    temp = ''
    for i in ip_l:
        bin_str = '{:0>8}'.format(bin(i).replace('0b', ''))
        temp += bin_str
    return bin_to_int(temp)


if __name__ == '__main__':

    try:
        lines = ['10.0.3.193', '167969729']
        ip, num = lines
        if not check_ip(ip):
            pass
        if not num.isdigit():
            pass
        ip_int = ip_to_int(ip)
        print(ip_int)
        int_s = '{:0>32}'.format(int_to_bin(int(num)))
        print(int_s)
        temp_ip = [int_s[i:i+8] for i in range(0, len(int_s), 8)]
        print(temp_ip)
        temp_ip = [str(bin_to_int(i)) for i in temp_ip]
        print('.'.join(temp_ip))

    except:
        raise