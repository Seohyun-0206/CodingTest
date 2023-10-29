n = int(input())

str = input()

val = [int(input()) for _ in range(n)]

stack = []

for s in str:
    if 'A' <= s <= 'Z':
        stack.append(val[ord(s) - ord('A')])
    else:
        s2 = stack.pop()
        s1 = stack.pop()

        if s == '+':
            stack.append(s1 + s2)
        elif s == '-':
            stack.append(s1 - s2)
        elif s == '*':
            stack.append(s1 * s2)
        elif s == '/':
            stack.append(s1 / s2)

print('%.2f' %stack[0])