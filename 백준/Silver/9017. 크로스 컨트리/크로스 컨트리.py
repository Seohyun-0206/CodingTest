import sys

t = int(input())

for _ in range(t):
    n = int(input())
    team = list(map(int, sys.stdin.readline().split()))

    count = {}
    for i in range(n):
        if team[i] in count:
            count[team[i]] += 1
        else:
            count[team[i]] = 1

    dele = []
    for k, v in count.items():
        if v < 6:
            dele.append(k)

    score = {}
    idx = 1
    for i in range(n):
        if team[i] not in dele:
            if team[i] in score:
                if score[team[i]][0] < 4:
                    score[team[i]][0] += 1
                    score[team[i]][1] += idx
                elif score[team[i]][0] == 4:
                    score[team[i]][0] += 1
                    score[team[i]][2] = idx
            else:
                score[team[i]] = [1, idx, 0]
            idx += 1

    score = sorted(score.items(), key=lambda x:(x[1][1], x[1][2]))

    print(score[0][0])

