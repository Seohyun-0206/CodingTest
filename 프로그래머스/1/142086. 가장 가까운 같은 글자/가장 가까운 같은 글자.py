def solution(s):
    n = len(s)
    answer = [-1] * n
    for i in range(n):
        idx = -1
        for j in range(i - 1, -1, -1):
            if s[j] == s[i]:
                idx = j
                break
        if idx > -1:
            answer[i] = i - idx
            
    return answer