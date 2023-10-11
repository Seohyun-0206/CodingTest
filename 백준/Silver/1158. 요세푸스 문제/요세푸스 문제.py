n, k = map(int, input().split())

s1 = [n - i for i in range(n)]
s2 = []
answer = []
while n > 0:
    for i in range(k - 1):
        if not s1:
            s1.extend(reversed(s2))
            s2 = []
        s2.append(s1.pop())

    if not s1:
        s1.extend(reversed(s2))
        s2 = []
    answer.append(s1.pop())
    n -= 1

print("<", ", ".join(map(str, answer)), ">", sep='')