import sys

str = sys.stdin.readline().rstrip()

stack = []
result = 0
for i in range(len(str)):
    if str[i] == '(':
        stack.append(str[i])
    else:
        stack.pop()
        if str[i - 1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)