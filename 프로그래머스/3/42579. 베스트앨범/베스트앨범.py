def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in dic1:
            dic1[g].append((i, p))
        else:
            dic1[g] = [(i, p)]
        
        if g in dic2:
            dic2[g] += p
        else:
            dic2[g] = p
        
    dic2 = sorted(dic2.items(), reverse=True, key=lambda x:x[1])
    for k, v in dic2:
        for i, p in sorted(dic1[k], reverse=True, key=lambda x:x[1])[:2]:
            answer.append(i)

    return answer