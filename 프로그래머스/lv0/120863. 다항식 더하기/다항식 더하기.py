def solution(polynomial):
    poly = list(polynomial.replace('+', ' ').split())
    cnt = 0
    n = 0
    for p in poly:
        if 'x' in p:
            if len(p) > 1:
                cnt += int(p[:-1])
        
            else:
                cnt += 1
        else:
             n += int(p)  
                
    if cnt > 0 and n > 0:
        if cnt > 1:
            answer = str(cnt) + "x + " + str(n)
        else:
            answer = "x + " + str(n)
    elif cnt > 0:
        if cnt > 1:
            answer = str(cnt) + "x"
        else:
            answer = "x"
    elif n > 0:
        answer = str(n)
    return answer