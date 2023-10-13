import itertools

height = [int(input()) for _ in range(9)]


h = list(itertools.combinations(height, 7))

result = []
for x in h:
       if sum(x) == 100:
              result = list(x)

result.sort()
for i in range(7):
       print(result[i])