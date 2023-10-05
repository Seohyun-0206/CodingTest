def solution(my_string):
    n = list(my_string.split())
    answer = int(n[0])
    for i in range(1, len(n) - 1, 2):
        if n[i] == '+':
            answer += int(n[i + 1])
        elif n[i] == '-':
            answer -= int(n[i + 1])
    return answer