from itertools import permutations
def solution(numbers):
    answer = []
    for p in permutations(numbers, 2):
        answer.append(sum(p))
        
    answer = sorted(list(set(answer)))
    return answer