def solution(num, k):
    return -1 if k not in list(map(int, str(num))) else list(map(int, str(num))).index(k) + 1