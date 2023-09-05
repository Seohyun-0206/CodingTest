dp = [0 for i in range(41)]

def fibo(n):
    if n == 0 or n == 1:
        return n

    if dp[n] != 0:
        return dp[n]

    dp[n] = fibo(n - 1) + fibo(n - 2)

    return dp[n]


t = int(input())

for i in range(t):
    n = int(input())
    if n == 0:
        print("1 0")
    else:
        print(fibo(n - 1), fibo(n))
