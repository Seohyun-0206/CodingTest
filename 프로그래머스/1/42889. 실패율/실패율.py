def solution(N, stages):
    dic = {}
    p = len(stages)
    
    for i in range(1, N + 1):
        if p != 0:
            dic[i] = stages.count(i) / p
            p -= stages.count(i)
        else:
            dic[i] = 0

    return sorted(dic, reverse=True, key=lambda x: dic[x])

#게임시간 늘려 난이도 조절 - 실패율 구하는 코드
# 실패율 = 노클리어/도달
