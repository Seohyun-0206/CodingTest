def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            r = yellow // i
            c = i
            if 2 * (r + c) + 4 == brown:
                return [r + 2, c + 2]