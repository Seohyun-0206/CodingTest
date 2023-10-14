from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
check = [False] * 100001
def bfs():
    q = deque([n])
    check[n] = True

    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for i in (2 * x, x - 1, x + 1):
            if 0 <= i <= 100000 and check[i] == False:
                q.append(i)
                check[i] = True
                if i == 2 * x:
                    visited[i] = visited[x]
                else:
                    visited[i] = visited[x] + 1

bfs()
