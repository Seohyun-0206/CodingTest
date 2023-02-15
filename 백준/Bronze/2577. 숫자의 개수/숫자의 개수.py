num = 1
for i in range(3):
    num *= int(input())

n = list(str(num))
for i in range(10):
    print(n.count(str(i)))