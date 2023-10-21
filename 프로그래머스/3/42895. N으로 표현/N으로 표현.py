def solution(N, number):
    dp = []
    
    for i in range(1, 9):
        x = set()
        x.add(int(str(N) * i))
        for j in range(0, i - 1):
            for a in dp[j]:
                for b in dp[-j-1]:
                    x.add(a + b)
                    x.add(a - b)
                    x.add(a * b)
                    if b != 0:
                        x.add(a // b)
        if number in x:
            return i
        dp.append(x)
    return -1