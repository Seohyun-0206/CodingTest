import sys
n = int(input())

for i in range(0, n):
    str = list(sys.stdin.readline().split())
    print(''.join(s[-1::-1] + ' ' for s in str))