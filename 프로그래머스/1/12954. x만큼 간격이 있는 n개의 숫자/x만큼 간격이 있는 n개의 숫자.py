def solution(x, n):
    answer = []
    cnt = 0
    i = x
    while cnt < n:
        answer.append(i)
        i += x
        cnt += 1
    return answer