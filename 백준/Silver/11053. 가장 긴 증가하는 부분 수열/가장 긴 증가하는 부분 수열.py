import sys
n = int(input())

A = list(map(int, sys.stdin.readline().split()))

d = [1] * 1001

for i in range(1, n):
    for j in range(0, i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))