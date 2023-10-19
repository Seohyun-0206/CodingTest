def solution(a, b, n):
    answer = 0
    while n >= a:
        d = n // a
        e = n - d * a
        n = d * b + e
        answer += d * b
    
    return answer