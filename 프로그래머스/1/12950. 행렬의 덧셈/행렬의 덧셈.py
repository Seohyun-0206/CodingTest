def solution(arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        sum = []
        for i, j in zip(a, b):
            sum.append(i + j)
        answer.append(sum)
    return answer