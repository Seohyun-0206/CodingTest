def solution(n):
    answer = []
    x = 2
    while x <= n:
        if n % x == 0:
            n //= x
            if x not in answer:
                answer.append(x)
        else:
               x += 1 
    return answer