import sys

n, k = map(int, input().split())

medal = [[] for _ in range(n)]

for _ in range(n):
    str = list(map(int, sys.stdin.readline().rstrip().split()))
    medal[str[0] - 1] = str[1:]

result = 1
for i in range(n):
    if i == k - 1:
        continue
    if medal[i][0] > medal[k - 1][0]:
        result += 1
    elif medal[i][0] == medal[k - 1][0] and medal[i][1] > medal[k - 1][1]:
        result += 1
    elif medal[i][0] == medal[k - 1][0] and medal[i][1] == medal[k - 1][1] and \
            medal[i][2] > medal[k - 1][2]:
        result += 1

print(result)