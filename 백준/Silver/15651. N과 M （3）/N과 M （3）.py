def solution(num):
    if num == m:
        print(" ".join(map(str, result)))
        return

    for i in range(n):
        result.append(i + 1)
        solution(num + 1)
        result.pop()


n, m = map(int, input().split())


result = []

solution(0)
