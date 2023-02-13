str = input().upper()

set_str = list(set(str))

cnt = []

for i in set_str:
    count = str.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(set_str[cnt.index(max(cnt))])