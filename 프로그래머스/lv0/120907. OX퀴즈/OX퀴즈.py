import re
def solution(quiz):
    q = [list(x.split(' ')) for x in quiz]
    answer = []
    for x in q:
        if x[1] == "+":
            result = int(x[0]) + int(x[2])
        else:
            result = int(x[0]) - int(x[2])
        if result == int(x[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer