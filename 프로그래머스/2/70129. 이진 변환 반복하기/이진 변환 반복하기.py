def solution(s):
    cnt = 0
    answer = 0
    while s != '1':
        print(s)
        cnt += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s))[2:])
        answer += 1
    
    return [answer, cnt]