def binary_search(A, x, s, e):
    while s <= e:
        mid = (s + e) // 2
        if x == A[mid]:
            return 1
        elif x > A[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return 0

n = int(input())

A = list(map(int, input().split()))
A = sorted(A)

m = int(input())

x = list(map(int, input().split()))

for i in x:
    print(binary_search(A, i, 0, n - 1))
