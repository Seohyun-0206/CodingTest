from collections import deque

def bfs(a, b):
    q = deque([(a, b)])

    graph[a][b] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    q.append([nx, ny])

    answer.append(cnt)

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)

answer.sort()
print(len(answer))
for i in answer:
    print(i)