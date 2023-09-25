def solution(array, n):
    answer = sum(1 for i in array if i == n)
    return answer