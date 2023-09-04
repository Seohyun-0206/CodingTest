from collections import deque
import sys

n = int(input())

de = deque()

for i in range(n):
    op = list(sys.stdin.readline().split())

    if op[0] == "push_back":
        de.append(int(op[1]))
    elif op[0] == "push_front":
        de.appendleft(int(op[1]))
    elif op[0] == "pop_front":
        if len(de) < 1:
            print(-1)
        else: print(de.popleft())
    elif op[0] == "pop_back":
        if len(de) < 1:
            print(-1)
        else: print(de.pop())
    elif op[0] == "size":
        print(len(de))
    elif op[0] == "empty":
        if len(de) < 1:
            print(1)
        else:
            print(0)
    elif op[0] == "front":
        if len(de) < 1:
            print(-1)
        else: print(de[0])
    elif op[0] == "back":
        if len(de) < 1:
            print(-1)
        else:
            print(de[len(de) - 1])