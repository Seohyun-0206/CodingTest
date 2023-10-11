import sys

str = list(sys.stdin.readline().rstrip())

array = []
s1 = ""
s2 = ""
for s in str:
    if s == '<':
        array.append(s1)
        s1 = ""
        s2 += s
        continue
    elif s == '>':
        s2 += s
        array.append(s2)
        s2 = ""
        continue
    if len(s2) > 0:
        s2 += s
    else:
        s1 += s

array.append(s1)

answer = []
for word in array:
    if '<' in word:
        answer.append(word)
    else:
        s = word.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]


        s = " ".join(s)
        answer.append(s)

print("".join(answer))
