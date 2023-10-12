import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

rank = [1] * n
for i in range(n):
    for j in range(n):
        if i != j and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[i] += 1


print(' '.join(map(str, rank)))