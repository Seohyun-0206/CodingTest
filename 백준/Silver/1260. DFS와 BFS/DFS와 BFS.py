from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, node, visited):
    visited[node] = True

    print(node, end=' ')

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited1 = [False] * (n + 1)
dfs(graph, v, visited1)
print()

visited2 = [False] * (n + 1)
bfs(graph, v, visited2)
