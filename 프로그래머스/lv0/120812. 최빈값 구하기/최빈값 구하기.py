def solution(array):
    num = set(array)
    max_count = -1
    for i in num:
        count = array.count(i)
        if count > max_count:
            max_count = count
            answer = i
        elif count == max_count:
            answer = -1
        
    return answer