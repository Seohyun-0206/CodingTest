def solution(prices):
    n = len(prices)
    answer = [i for i in range(n - 1, -1, -1)]
    s = []

    for i in range(n):
        while s and prices[s[-1]] > prices[i]:
            idx = s.pop()
            answer[idx] = i - idx
        s.append(i)
            
    return answer