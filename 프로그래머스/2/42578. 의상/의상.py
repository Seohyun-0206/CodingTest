def solution(clothes):
    answer = 1
    dic = {}
    
    for c in clothes:
        if c[1] in dic:
            dic[c[1]].append(c[0])
        else:
            dic[c[1]] = [c[0]]
            
    for d in dic:
        answer *= (len(dic[d]) + 1)
    return answer - 1