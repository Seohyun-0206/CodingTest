def solution(emergency):
    answer = []
    for i in emergency:
        cnt = 0
        for j in emergency:
            if i <= j:
                cnt += 1
        answer.append(cnt)
            
    return answer