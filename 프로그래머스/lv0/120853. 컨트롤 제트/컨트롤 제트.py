def solution(s):
    answer = 0
    s = list(s.split())
    x = 0
    for i in s:
        if i != 'Z':
            x = int(i)
            answer += x
        else:
            answer -= x
            x = 0
    return answer