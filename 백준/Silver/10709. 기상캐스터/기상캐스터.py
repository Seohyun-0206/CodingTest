import sys

H, W = map(int, input().split())
clouds = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

answer = [[0] * W for _ in range(H)]
for i in range(H):
    cnt = 1
    cloud = False
    for j in range(W):
        if not cloud and clouds[i][j] == '.':
            answer[i][j] = -1
        elif clouds[i][j] == 'c':
            cloud = True
            cnt = 1
            answer[i][j] = 0
        elif cloud and clouds[i][j] == '.':
            answer[i][j] = cnt
            cnt += 1


for i in range(H):
    print(' '.join(map(str, answer[i])))