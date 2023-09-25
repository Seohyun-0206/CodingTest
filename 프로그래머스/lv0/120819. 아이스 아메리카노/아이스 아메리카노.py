def solution(money):
    cnt = money // 5500
    answer = [cnt, money - cnt * 5500]
    return answer