
m, n = map(int, input().split())
goods = {}
for i in range(1, n+1):
    v, p, q = map(int, input().split())
    goods[i] = (v, p, q)
f = [0 for _ in range(m+1)]
for k, v in goods.items():
    for i in range(m, 0, -1):
        # 主件
        if v[2] == 0:
            if i >= v[0]:
                f[i] = max(f[i], f[i-v[0]] + v[0] * v[1])
            else:
                break
        # 附件
        else:
            if i >= v[0] + goods[v[2]][0]:
                f[i] = max(f[i], f[i-v[0]-goods[v[2]][0]] + v[0]*v[1] + goods[v[2]][0] * goods[v[2]][1])
            else:
                break
print(f[-1])
