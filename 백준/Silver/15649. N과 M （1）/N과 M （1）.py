import itertools

n, m = map(int, input().split())

arr = [i + 1 for i in range(n)]

num = list(itertools.permutations(arr, m))

for x in num:
       print(*x)


