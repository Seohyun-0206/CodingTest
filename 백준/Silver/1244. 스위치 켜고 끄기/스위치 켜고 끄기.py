n = int(input())
switch = list(map(int, input().split()))
s = int(input())
students = []
for _ in range(s):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num - 1, n, num):
            switch[i] = 1 if switch[i] == 0 else 0
    elif sex == 2:
        switch[num - 1] = 1 if switch[num - 1] == 0 else 0
        for i in range(1, n // 2 + 1):
            left = num - 1 - i
            right = num - 1 + i
            if left < 0 or right == n:
                break
            elif switch[left] == switch[right]:
                switch[left] = switch[right] = 1 if switch[left] == 0 else 0
            else:
                break

for i in range(n):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()