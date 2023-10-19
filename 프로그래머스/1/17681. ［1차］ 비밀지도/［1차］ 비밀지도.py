def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result = ''
        cnt = 0
        while cnt < n:
            if arr1[i] % 2 == 1 or arr2[i] % 2 == 1:
                result += '#'
            else:
                result += ' '
            arr1[i] //= 2
            arr2[i] //= 2
            cnt += 1
        answer.append(result[::-1])
    return answer