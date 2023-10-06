def solution(score):
    avg = [(e + m) / 2 for e, m in score]
    answer = [1] * len(avg)
    for i in range(0, len(avg)):
        for j in avg:
            if avg[i] < j:
                answer[i] += 1
    return answer