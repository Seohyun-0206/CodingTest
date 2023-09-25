def solution(num_list):
    even = [i for i in num_list if i % 2 == 0]
    length = len(even)
    answer = [length, len(num_list) - length]
    return answer