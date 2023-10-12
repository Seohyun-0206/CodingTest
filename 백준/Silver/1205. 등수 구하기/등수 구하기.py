import sys

n, t, p = map(int, sys.stdin.readline().split())

if n == 0:
    print(1)
else:
    ranking = list(map(int, sys.stdin.readline().split()))
    if n == p and ranking[-1] >= t:
        print(-1)
    else:
        rank = n + 1
        for i in range(n):
            if ranking[i] <= t:
                rank = i + 1
                break
        print(rank)
