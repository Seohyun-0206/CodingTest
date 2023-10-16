N = int(input())

cnt = N
for _ in range(N):
    arr = list(input())
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            pass
        elif arr[i] in arr[i + 1:]:
            cnt -= 1
            break

print(cnt)