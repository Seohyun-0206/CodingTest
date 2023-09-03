n, k = map(int, input().split())

queue = [i + 1 for i in range(n)]

arr = []
for i in range(n):
    for j in range(k-1):
        x = queue.pop(0)
        queue.append(x)

    arr.append(queue.pop(0))

print("<", end="")
for i in range(n - 1):
    print(arr[i], end=", ")

print(str(arr[n - 1]) + ">")