import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))

d = [1] * n

for i in range(0, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))