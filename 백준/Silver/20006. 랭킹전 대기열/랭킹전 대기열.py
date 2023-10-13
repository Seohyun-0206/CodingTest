p, m = map(int, input().split())

rooms = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m:
            continue

        if rooms[i][0] - 10 <= l <= rooms[i][0] + 10:
            rooms[i][1].append([l, n])
            flag = True
            break

    if not flag:
        rooms.append([l, [[l, n]]])

for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
        print('Started!')
        room = sorted(rooms[i][1], key=lambda x:x[1])
        for j in range(m):
            print(*room[j])
    else:
        print('Waiting!')
        room = sorted(rooms[i][1], key=lambda x:x[1])
        for j in range(len(rooms[i][1])):
            print(*room[j])

