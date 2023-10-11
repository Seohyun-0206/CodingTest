import sys
str1 = list(sys.stdin.readline().rstrip())
str2 = []
m = int(input())
for i in range(0, m):
    order = sys.stdin.readline().split()
    if order[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif order[0] == 'D':
        if str2:
            str1.append(str2.pop())
    elif order[0] == 'B':
        if str1:
            str1.pop()
    elif order[0] == 'P':
        str1.append(order[1])

print(''.join(str1 + list(reversed(str2))))