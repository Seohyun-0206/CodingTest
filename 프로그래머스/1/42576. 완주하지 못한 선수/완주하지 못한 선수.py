def solution(participant, completion):
    answer = ''
    dic = {}
    
    for p in participant:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
            
    for c in completion:
        if c in dic:
            dic[c] -= 1
    
    dic = sorted(dic.items(), key=lambda x:-x[1])
    return dic[0][0]