str = list(input())

num = {2:['A', 'B', 'C'],
       3:['D', 'E', 'F'],
       4:['G', 'H', 'I'],
       5:['J', 'K', 'L'],
       6:['M', 'N', 'O'],
       7:['P', 'Q', 'R', 'S'],
       8:['T', 'U', 'V'],
       9:['W', 'X', 'Y', 'Z']}

result = 0
for s in str:
    for i in range(2, 10):
        if s in num[i]:
            result += i + 1

print(result)