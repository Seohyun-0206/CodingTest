import sys
n = int(input())

d = [[0, 0, 0] for _ in range(91)]

d[1] = [1, 0, 1]
d[2] = [1, 1, 0]

for i in range(3, n + 1):
    d[i][1] = d[i - 1][0]
    d[i][2] = d[i - 1][0] - d[i - 1][2]
    d[i][0] = d[i][1] + d[i][2]

print(d[n][0])