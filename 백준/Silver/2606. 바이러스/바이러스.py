from collections import deque
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append(1)
visited[1] = 1

while q:
    v = q.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)

print(visited.count(1) - 1)