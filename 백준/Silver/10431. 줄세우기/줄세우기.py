import sys

p = int(sys.stdin.readline())

for _ in range(p):
    result = 0
    keys = list(map(int, sys.stdin.readline().split()))
    T, key = keys[0], keys[1:]
    for i in range(1, 20):
        min, m = -1, max(key) + 1
        for j in range(i):
            if key[i] < key[j] and key[j] < m:
                m = key[j]
                min = j
        if min != -1:
            result += (i - min)
            key = key[:min] + [key[i]] + key[min:i] + key[i + 1:]

    print(T, result)