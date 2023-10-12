import itertools
def solution(numbers):
    answer = 0
    
    num = list(numbers)
    per = []
    for i in range(1, len(num) + 1):
        per += itertools.permutations(num, i)
    
    num_per = []
    for i in per:
        num_per.append(''.join(i))
    num = list(set(map(int, num_per)))
    
    for n in num:
        if n > 1:
            if is_prime_number(n):
                answer += 1
    return answer

def is_prime_number(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True