n = int(input())

num = list(map(int, input().split()))
result = [-1 for _ in range(n)]
stack = [0]
for i in range(1, n):
    while stack and num[stack[-1]] < num[i]:
        result[stack.pop()] = num[i]
    stack.append(i)

print(' '.join(map(str, result)))