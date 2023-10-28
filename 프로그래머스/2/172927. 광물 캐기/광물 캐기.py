def solution(picks, minerals):
    answer = 0
    
    sum = 0
    for p in picks:
        sum += p
    
    if len(minerals) > sum * 5:
        minerals = minerals[:sum * 5]

    mine = [[0] * 3 for _ in range(10)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            mine[i // 5][0] += 1
        elif minerals[i] == 'iron':
            mine[i // 5][1] += 1
        elif minerals[i] == 'stone':
            mine[i // 5][2] += 1

    mine.sort(reverse=True, key=lambda x:(x[0], x[1], x[2]))

    for m in mine:
        d, i, s = m
        for j in range(3):
            if j == 0 and picks[j] > 0:
                picks[j] -= 1
                answer += d + i + s
                break
            elif j == 1 and picks[j] > 0:
                picks[j] -= 1
                answer += (d * 5) + i + s
                break
            elif j == 2 and picks[j] > 0:
                picks[j] -= 1
                answer += (d * 25) + (i * 5) + s
    return answer