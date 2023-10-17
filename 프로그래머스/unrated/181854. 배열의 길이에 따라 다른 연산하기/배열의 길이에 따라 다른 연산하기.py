def solution(arr, n):
    if len(arr) % 2 == 0:
        arr = [arr[i] + n if i % 2 != 0 else arr[i] for i in range(len(arr))]
    else:
        arr = [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))]
    return arr