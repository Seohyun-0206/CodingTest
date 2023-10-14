def solution(num):
    if num == m:
        print(" ".join(map(str, result)))
        return

    for i in range(n):
        if visited[i] == False:
            if i > 0 and visited[i - 1] == False and nums[i - 1] == nums[i]:
                continue
            visited[i] = True
            result.append(nums[i])
            solution(num + 1)
            visited[i] = False
            result.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = []
visited = [False] * len(nums)
solution(0)
