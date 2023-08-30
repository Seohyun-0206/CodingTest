def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j = 0, 0
    # 정렬 배열 생성
    sorted_arr = []

    # 합치면서 정렬하기
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 나머지 데이터 삽입
    sorted_arr += left[i:]
    sorted_arr += right[j:]

    return sorted_arr

n = int(input())

num = []

for _ in range(n):
    num.append(int(input()))


arr = merge_sort(num)

for i in arr:
    print(i)

