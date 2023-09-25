def solution(numbers):
    numbers.sort()
    a1 = numbers[0] * numbers[1]
    a2 = numbers[-1] * numbers[-2]
    return a1 if a1 > a2 else a2