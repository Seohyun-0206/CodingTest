import sys
m = int(input())

S = set()
nums = [i + 1 for i in range(20)]
for _ in range(m):
    str = sys.stdin.readline().split()
    if str[0] == "add":
        S.add(int(str[1]))
    elif str[0] == "remove":
        S.discard(int(str[1]))
    elif str[0] == "check":
        if int(str[1]) in S:
            print(1)
        else:
            print(0)
    elif str[0] == "toggle":
        if int(str[1]) in S:
            S.discard(int(str[1]))
        else:
            S.add(int(str[1]))
    elif str[0] == "all":
        S.update(nums)
    elif str[0] == "empty":
        S = set()