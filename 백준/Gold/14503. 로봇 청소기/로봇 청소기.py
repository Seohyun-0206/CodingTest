n, m = map(int, input().split())

r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0] #북, 동, 남, 서
dy = [0, 1, 0, -1]

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

room[r][c] = -1
cnt = 1
while room[r][c] != 1:

    flag = True
    for i in range(4):
        d -= 1
        if d == -1:
             d = 3
        if room[r + dx[d]][c + dy[d]] == 0:
            r += dx[d]
            c += dy[d]
            room[r][c] = -1
            cnt += 1
            flag = False
            break

    if flag:
        r += dx[(d + 2) % 4]
        c += dy[(d + 2) % 4]

print(cnt)