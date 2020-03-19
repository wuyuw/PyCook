
n, m = 4, 5

w = [1, 2, 3, 4]
v = [2, 4, 4, 5]


f = [0 for i in range(m+1)]
for i in range(n):
    for j in range(m, 0, -1):
        if j >= w[i]:
            f[j] = max(f[j], f[j-w[i]] + v[i])
        else:
            break
print(f[-1])
