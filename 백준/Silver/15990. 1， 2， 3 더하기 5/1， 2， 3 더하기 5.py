import sys
t = int(input())

d = [[0] * 4 for _ in range(100001)]

d[1] = [1, 1, 0, 0]
d[2] = [1, 0, 1, 0]
d[3] = [3, 1, 1, 1]
for i in range(4, 100001):
    result = 0
    for j in range(1, 4):
        d[i][j] = d[i - j][0] - d[i - j][j]
        result += d[i][j]

    d[i][0] = result % 1000000009

for i in range(t):
    n = int(input())
    print(d[n][0])