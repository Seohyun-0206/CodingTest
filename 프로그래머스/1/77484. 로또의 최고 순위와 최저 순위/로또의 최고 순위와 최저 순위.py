def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1
        
            
    return [rank[cnt + lottos.count(0)], rank[cnt]]