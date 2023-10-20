def solution(nums):
    n = len(nums) // 2
    set_n = set(nums)

    return min(n, len(set_n))