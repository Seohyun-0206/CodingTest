def solution(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
        if fac == n:
            return i
        elif fac > n:
            return i - 1