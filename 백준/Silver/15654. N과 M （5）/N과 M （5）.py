def solution(num):
    if num == m:
        print(" ".join(map(str, result)))
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(nums[i])
            solution(num + 1)
            visited[i] = False
            result.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False] * n
result = []

solution(0)
