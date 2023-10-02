def solution(my_string):
    answer = ''
    
    for i in range(0, len(my_string)):
        if my_string[i] not in my_string[:i]:
            answer += my_string[i]
    return answer