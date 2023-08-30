import sys

n = int(input())

count = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

# 데이터 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i)