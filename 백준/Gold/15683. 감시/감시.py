import copy
n, m = map(int, input().split())

office = []
cctv = []
result = 1e9
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list((map(int, input().split())))
    office.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j]) #cctv 종류와 좌표 저장


def fill(office, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if office[nx][ny] == 6:
                break
            elif office[nx][ny] == 0:
                office[nx][ny] = -1


def dfs(d, office):
    global result
    if d == len(cctv):
        count = 0
        for i in range(n):
            count += office[i].count(0)
        result = min(result, count)
        return

    tmp = copy.deepcopy(office)
    cctv_num, x, y = cctv[d]
    for i in mode[cctv_num]:
        fill(tmp, i, x, y)
        dfs(d + 1, tmp)
        tmp = copy.deepcopy(office)

dfs(0, office)
print(result)
