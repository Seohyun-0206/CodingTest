str = input()

dic = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
answer = []
stack = []

for s in str:
    if 'A' <= s <= 'Z':
        answer.append(s)
    elif s == '(':
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    else:
        while stack and dic[s] <= dic[stack[-1]]:
            answer.append(stack.pop())
        stack.append(s)

while len(stack) != 0:
    answer.append(stack.pop())

print(''.join(answer))