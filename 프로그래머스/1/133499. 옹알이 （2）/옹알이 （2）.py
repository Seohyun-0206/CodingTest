import re
def solution(babbling):
    ex = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for e in ex:
            if e*2 not in b:
                b = b.replace(e, ' ')
        if len(b.strip()) == 0:
            answer += 1
        
    return answer