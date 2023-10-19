def solution(name, yearning, photo):
    p = len(photo)
    answer = [0] * p
    
    for i in range(p):
        for j in range(len(name)):
            if name[j] in photo[i]:
                answer[i] += yearning[j]
    return answer