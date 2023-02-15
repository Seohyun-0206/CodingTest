S = input()

a = 'abcdefghijklmnopqrstuvwxyz'

cnt = [-1 for i in range(len(a))]

for i in range(len(S)):
    if cnt[a.index(S[i])] == -1:
        cnt[a.index(S[i])] = i

for i in cnt:
    print(i, end=" ")
