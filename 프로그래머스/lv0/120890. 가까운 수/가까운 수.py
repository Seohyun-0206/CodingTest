def solution(array, n):
    array.sort()
    min = 101
    min_i = 0
    for i in array:
        if min > abs(i - n):
            min = abs(i - n)
            min_i = i
    return min_i