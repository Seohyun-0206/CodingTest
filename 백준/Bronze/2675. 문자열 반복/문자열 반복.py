n = int(input())

for i in range(n):
    c, str = input().split()
    num = int(c)
    result = ''
    for j in str:
        result += j * num
    print(result)