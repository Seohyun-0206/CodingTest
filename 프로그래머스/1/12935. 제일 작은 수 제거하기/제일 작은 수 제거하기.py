def solution(arr):
    m = min(arr)
    return [i for i in arr if i != m] if len(arr) > 1 else [-1]