m, n = map(int, input().split())

arr = [0] * (n + 1)
arr[0] = arr[1] = 1

for i in range(2, n + 1):
    for j in range(i*2, n + 1, i):
        if arr[j] == 0:
            arr[j] = 1

for i in range(m, n + 1):
    if arr[i] == 0:
        print(i)

