import sys

H, W = map(int, input().split())
clouds = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

answer = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if clouds[i][j] == 'c':
            answer[i][j] = 0
            continue
        if 'c' in clouds[i][:j]:
            cloud = -1
            for k in range(j - 1, -1, -1):
                if clouds[i][k] == 'c':
                    cloud = k
                    break
            answer[i][j] = j - k
        else:
            answer[i][j] = -1

for i in range(H):
    print(' '.join(map(str, answer[i])))