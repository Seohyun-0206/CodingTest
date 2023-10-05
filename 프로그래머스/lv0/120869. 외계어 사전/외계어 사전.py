def solution(spell, dic):
    answer = 2
    for word in dic:
        flag = 0
        for s in spell:
            if s not in word:
                flag = 1
                break
        if flag == 0:
            answer = 1
            break
        
    return answer