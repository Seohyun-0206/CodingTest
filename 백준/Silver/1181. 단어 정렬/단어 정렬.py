n = int(input())

str = [input() for _ in range(n)]
str = list(set(str))

sort_str = []
for i in str:
    sort_str.append((len(i), i))

result = sorted(sort_str)

for len, word in result:
    print(word)
