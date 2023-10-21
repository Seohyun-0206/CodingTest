from collections import deque

def bfs(a, b, c):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] > c:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

n = int(input())

graph = []
m = -1
for i in range(n):
    graph.append(list(map(int, input().split())))
    m = max(m, max(graph[i]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for i in range(m):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1

    result = max(result, cnt)

print(result)