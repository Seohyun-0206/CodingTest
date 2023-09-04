import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

rank = [1] * n
for i in range(n):
    for j in arr:
        if arr[i][0] < j[0] and arr[i][1] < j[1]:
            rank[i] += 1


for i in range(n):
    print(rank[i], end=' ')