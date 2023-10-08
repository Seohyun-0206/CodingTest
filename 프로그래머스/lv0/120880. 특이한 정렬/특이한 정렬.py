def solution(numlist, n):
    rank = {}
    for i in numlist:
        rank[i] = abs(n - i)
    r = dict(sorted(rank.items(), key=lambda x:(x[1], -x[0])))
    return list(r.keys())