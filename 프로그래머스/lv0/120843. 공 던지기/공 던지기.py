def solution(numbers, k):
    answer = 1
    for i in range(0, k-1):
        answer += 2
        if answer > len(numbers):
            answer %= len(numbers)
        
    return answer