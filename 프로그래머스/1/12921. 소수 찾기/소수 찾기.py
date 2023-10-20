def solution(n):
    num = [1] * (n + 1)
    num[0] = 0
    num[1] = 0
    
    for i in range(2, n + 1):
        if num[i] == 1:
            for j in range(2*i, n + 1, i):
                num[j] = 0
        
    return num.count(1)