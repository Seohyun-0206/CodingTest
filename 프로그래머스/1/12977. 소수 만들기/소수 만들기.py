from itertools import combinations
def solution(nums):
    prime = []
    
    for a, b, c in combinations(nums, 3):
        s = a + b + c
        flag = 0
        for i in range(2, int(s**0.5) + 1):
            if s % i == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(s)
        

    return len(prime)