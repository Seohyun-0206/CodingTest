n = int(input())

stack = []
cal = []
num = 1
flag = 0

for i in range(0, n):
    x = int(input())

    while num <= x:
        stack.append(num)
        cal.append("+")
        num += 1

    if stack[-1] == x:
        stack.pop()
        cal.append("-")
    else:
        flag = 1
        break

if flag == 1:
    print("NO")
else:
    print("\n".join(cal))