def solution(num):
    if num == m:
        print(" ".join(map(str, result)))
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            result.append(i + 1)
            solution(num + 1)
            visited[i] = False
            result.pop()

n, m = map(int, input().split())

visited = [False] * (n + 1)

result = []

solution(0)
