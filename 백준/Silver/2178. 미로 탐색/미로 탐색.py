from collections import deque
n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

q = deque()
q.append((0, 0))
visited[0][0] = True

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and miro[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1

print(miro[n - 1][m - 1])