str = input().upper()

set_str = list(set(str))

cnt = []
for i in set_str:
    cnt.append(str.count(i))


if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(set_str[cnt.index(max(cnt))])