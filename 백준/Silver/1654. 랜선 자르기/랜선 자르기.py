k, n = map(int, input().split())

length = [int(input()) for _ in range(k)]

min_len, max_len = 1, max(length)

while min_len <= max_len:
    mid = (min_len + max_len) // 2
    cnt = 0
    for i in length:
        cnt += i // mid

    if cnt >= n:
        min_len = mid + 1
    else:
        max_len = mid -1

print(max_len)

