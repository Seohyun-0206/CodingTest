import sys
n = int(input())
p = [0] + list(map(int, sys.stdin.readline().split()))

d = [0] * 1001
for i in range(1, n + 1):
    d[i] = p[i]
    for j in range(1, i):
        d[i] = max(d[i - j] + p[j], d[i])

print(d[n])