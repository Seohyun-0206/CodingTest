num = int(input())

score = list(map(int, input().split()))

max_sco = max(score)

sco = [i / max_sco * 100 for i in score]

avg = sum(sco) / num

print(avg)