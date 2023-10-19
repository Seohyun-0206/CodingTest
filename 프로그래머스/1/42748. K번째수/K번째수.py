def solution(array, commands):
    answer = []
    for c in commands:
        new = sorted(array[c[0] - 1:c[1]])
        answer.append(new[c[2] - 1])
    return answer