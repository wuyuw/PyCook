import bisect


def deal(l):
    # 每次向b中加一个list中的元素
    b = [9999]*len(l)
    b[0] = l[0]
    res = [1]
    for i in range(1,len(l)):
        pos = bisect.bisect_left(b,l[i])
        res += [pos+1]
        b[pos]=l[i]
    return res


def deal2(l):
    sub = []
    res = []
    for i in range(len(l)):
        pos = bisect.bisect_left(sub, l[i])
        res.append(pos+1)
        if pos >= len(sub):
            sub.append(l[i])
        else:
            sub[pos] = l[i]
    return res


l = [186, 186, 150, 200, 160, 130, 197, 200]

r = deal(l)
print(r)
r2 = deal(l)
print(r2)