import math
def solution(n):
    answer = -1
    i = 1
    while i**2 <= n:
        if i**2 == n:
            answer = (i + 1)**2
        i += 1

    return answer