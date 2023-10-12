A, B, C = map(int, input().split())

time = [0] * 101
max_ = 0
min_ = 101
for _ in range(3):
    a, l = map(int, input().split())
    for i in range(a, l):
        time[i] += 1
    max_ = max(l, max_)
    min_ = min(a, min_)

result = 0
for i in range(min_, max_):
    if time[i] == 1:
        result += A
    elif time[i] == 2:
        result += B * 2
    elif time[i] == 3:
        result += C * 3

print(result)

