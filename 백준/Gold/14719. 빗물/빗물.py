H, W = map(int, input().split())

block = list(map(int, input().split()))

left, right = 0, W - 1
max_left = block[left]
max_right = block[right]

cnt = 0
while left < right:
    max_left = max(max_left, block[left])
    max_right = max(max_right, block[right])

    if max_left >= max_right:
        cnt += max_right - block[right]
        right -= 1
    if max_right > max_left:
        cnt += max_left - block[left]
        left += 1

print(cnt)