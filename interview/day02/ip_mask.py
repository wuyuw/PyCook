
from collections import Counter
import bisect



def check_ip(ip):
    ip_l = ip.split('.')
    if len(ip_l) != 4:
        return False
    for i in ip_l:
        if not i.isdigit():
            return False
        if str(int(i)) != i:
            return False
        if int(i) < 0 or int(i) > 255:
            return False
    return True


ml = [255 ^ (255 >> i) for i in range(8)]


def check_mask(ms):
    def _check_ms(l, start):
        if start == len(l) -1:
            if l[start] in ml:
                return True
            return False
        if l[start] == 255:
            start += 1
            return _check_ms(l, start)
        elif l[start] in ml and len(set(l[start+1:])) == 1 and l[start+1] == 0:
            return True
        else:
            return False
    if not check_ip(ms):
        return False
    ms_l = list(map(int, ms.split('.')))
    if len(set(ms_l)) == 1 and ms_l[0] in (0, 255):
        return False
    return _check_ms(ms_l, 0)


def main():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    err = 0
    pri = 0


    while True:
        line = input()
        if not line:
            break
        ip, ms = line.split('~')
        if not check_ip(ip) or not check_mask(ms):
            err += 1
            continue
        ip = list(map(int, ip.split('.')))
        ip_f = ip[0]
        if ip_f < 127:
            a += 1
        elif ip_f > 127 and ip_f <= 191:
            b += 1
        elif ip_f <= 223:
            c += 1
        elif ip_f <= 239:
            d += 1
        if ip_f >= 240:
            e += 1
        if ip_f == 10 or \
            (ip_f == 172 and ip[1] >= 16 and ip[1] <= 31) or \
            (ip_f == 192 and ip[1] == 168):
            pri += 1
    print(a, b, c, d, e, err, pri)


if __name__ == '__main__':
    main()
