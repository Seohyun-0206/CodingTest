def solution(my_string):
    answer = 0
    sum = 0
    for i in my_string:
        if i.isdigit():
            sum *= 10
            sum += int(i)
        else:
            answer += sum
            sum = 0
    if my_string[-1].isdigit():
        answer += sum
    return answer