from collections import deque

n = int(input())

queue = deque([n - i for i in range(n)])

while len(queue) > 1:
    queue.pop()
    x = queue.pop()
    queue.appendleft(x)

print(queue[0])