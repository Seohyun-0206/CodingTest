from collections import deque

n, k = map(int, input().split())

MAX = 100000
visited = [0] * (MAX + 1)

def bfs(n, k, visited):
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            print(visited[now])
            break

        for j in (now - 1, now + 1, 2 * now):
            if 0 <= j <= MAX and visited[j] == 0:
                visited[j] = visited[now] + 1
                q.append(j)

bfs(n, k, visited)