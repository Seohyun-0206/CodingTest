n = int(input())

m = 0
for i in range(1, n+1):
    num = list(map(int, str(i)))
    result = i + sum(num)
    if n == result:
        m = i
        break
print(m)