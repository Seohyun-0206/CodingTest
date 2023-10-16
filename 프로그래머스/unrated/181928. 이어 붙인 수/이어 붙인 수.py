def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        if i % 2 != 0:
            odd *= 10
            odd += i
        else:
            even *= 10
            even += i
    return even + odd