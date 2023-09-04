from math import inf

n, m, b = map(int, input().split())

arr = []

for i in range(n):
    arr += list(map(int, input().split()))

max_h = max(arr)
min_h = min(arr)
min_time = inf
for i in range(max_h, min_h - 1, -1):
    time = 0
    k = b
    for j in arr:
        if j > i :
            k += (j - i)
            time += 2 * (j - i)
        elif j < i:
            k -= (i - j)
            time += (i - j)

    if k >= 0 and time < min_time:
        min_time = time
        height = i

print(min_time, height)

