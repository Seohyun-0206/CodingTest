from itertools import combinations
def solution(numbers):
    answer = []
    for p in combinations(numbers, 2):
        answer.append(sum(p))
        
    answer = sorted(list(set(answer)))
    return answer