n = int(input())

winning = {1:[0, 0], 2:[0, 0]}

prev = 0
win = 0
for _ in range(n):
    t, h = input().split()
    m, s = map(int, h.split(':'))
    t = int(t)
    winning[t][0] += 1

    time = m * 60 + s
    if winning[1][0] == winning[2][0]:
        if win != 0:
            winning[win][1] += time - prev
        win = 0
    elif winning[1][0] > winning[2][0]:
        if win == 0:
            prev = time
            win = 1
    else:
        if win == 0:
            prev = time
            win = 2

if win != 0:
    winning[win][1] += 48 * 60 - prev

print(f'%02d:%02d' %(winning[1][1] // 60, winning[1][1] % 60))
print(f'%02d:%02d' %(winning[2][1] // 60, winning[2][1] % 60))