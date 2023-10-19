def solution(k, score):
    answer = []
    result = []
    for i in range(len(score)):
        if len(result) < k:
            result.append(score[i])
        elif result[-1] < score[i]:
            result[-1] = score[i]
        result = sorted(result, reverse=True)
        answer.append(result[-1])
        
    return answer