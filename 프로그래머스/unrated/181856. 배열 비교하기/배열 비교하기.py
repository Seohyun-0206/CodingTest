def solution(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    if len1 > len2:
        return 1
    elif len1 < len2:
        return -1
    else:
        s1 = sum(arr1)
        s2 = sum(arr2)
        if s1 > s2:
            return 1
        elif s1 < s2:
            return -1
    return 0