str = input()

alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

result = 0
i = 0

while i < len(str):
    flag = 0
    for a in alpha:
        n = len(a)
        if str[i:i+n] == a:
            i += n
            flag = 1
            break
    if flag == 0:
        i += 1
    result += 1

print(result)