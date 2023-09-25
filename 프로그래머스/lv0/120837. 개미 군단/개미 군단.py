def solution(hp):
    attack = [5, 3, 1]
    answer = 0
    for i in attack:
        answer += hp // i
        hp %= i
    return answer