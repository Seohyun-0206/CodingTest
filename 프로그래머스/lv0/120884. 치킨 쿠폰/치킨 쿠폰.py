def solution(chicken):
    answer = 0
    while chicken >= 10:
        service = chicken // 10
        chicken = chicken - service * 10 + service
        answer += service
    
    return answer
