from collections import deque

n, k = map(int, input().split())

loc = [0] * 100001
visited = [0] * 100001
result = []
def bfs():
    q = deque([n])

    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            tmp = x
            for _ in range(visited[x] + 1):
                result.append(tmp)
                tmp = loc[tmp]

            print(' '.join(map(str, result[::-1])))
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
                loc[i] = x

bfs()
