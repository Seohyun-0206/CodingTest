import sys

#같은 눈 3개 -> 10000 + 눈 * 1000
#같은 눈 2개 -> 1000 + 눈 * 100
#모두 다른 눈 -> 가장 큰 눈 * 100

x, y, z = map(int, input().split())

if x == y and x == z:
    print(10000 + x * 1000)
elif x == y and x != z:
    print(1000 + x * 100)
elif x == z and x != y:
    print(1000 + x * 100)
elif y == z and y != x:
    print(1000 + y * 100)
else:
    m = max(max(x, y), z)
    print(m * 100)