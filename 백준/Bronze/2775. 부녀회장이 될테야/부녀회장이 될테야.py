d = [[0 for i in range(15)] for j in range(15)]

def dp(k, n):
    if k == 0:
        d[k][n] = n
        return d[k][n]

    if d[k][n] != 0:
        return d[k][n]

    for i in range(1, n + 1):
        d[k][n] += dp(k - 1, i)

    return d[k][n]


t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    print(dp(k, n))