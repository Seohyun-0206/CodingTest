def solution(num):
    if num == m:
        print(" ".join(map(str, result)))
        return

    for i in range(n):
        result.append(nums[i])
        solution(num + 1)
        result.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = []

solution(0)
