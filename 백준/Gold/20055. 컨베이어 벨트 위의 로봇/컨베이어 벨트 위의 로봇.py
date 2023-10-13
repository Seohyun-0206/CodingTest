from collections import deque

n, k = map(int, input().split())

A = deque(list(map(int, input().split())))
belt = deque([False] * n)

cnt = 0
while True:
    cnt += 1

    A.rotate(1)
    belt.rotate(1)

    belt[n - 1] = False #내려야할 로봇은 내리기

    for i in range(n - 2, -1, -1):
        if belt[i] and not belt[i + 1] and A[i + 1] >= 1:
            belt[i + 1], belt[i] = True, False
            A[i + 1] -= 1

    belt[n - 1] = False

    if A[0] >= 1:
        belt[0] = True
        A[0] -= 1

    if A.count(0) >= k:
        break
print(cnt)