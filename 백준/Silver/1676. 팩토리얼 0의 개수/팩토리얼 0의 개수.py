n = int(input())

x = 1
for i in range(1, n + 1):
    x *= i

cnt = 0

while x > 0:
    if x % 10 == 0:
        x //= 10
        cnt += 1
    else:
        print(cnt)
        break