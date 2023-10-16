def solution(my_string, is_suffix):
    n = len(my_string)
    m = len(is_suffix)
    return 1 if my_string[n - m:] == is_suffix else 0