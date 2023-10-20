def solution(dartResult):
    n = ''
    result = []
    for d in dartResult:
        if d.isdigit():
            n += d
        elif d == 'S':
            result.append(int(n))
            n = ''
        elif d == 'D':
            result.append(int(n)**2)
            n = ''
        elif d == 'T':
            result.append(int(n)**3)
            n = ''
        elif d == '*':
            if len(result) > 1:
                result[-2] *= 2
            result[-1] *= 2
        elif d == '#':
            result[-1] *= -1
            
    
    print(result)
    return sum(result)

# 3번 0~10점
# s = 점 d = 점**2 t = 점**3
# *스타상 = 현점수, 전점수 2배 중첩시 배수 증가
# #아차상 = 현점수 마이너스 스타상과 중첩 - 아차상 -2배

