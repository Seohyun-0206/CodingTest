def solution(park, routes):
    n = len(park)
    m = len(park[0])
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = {"N":0, "E":1, "S":2, "W":3}
    
    start = [0, 0]
    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                start = [i, j]
                
    for r in routes:
        str = list(r.split())
        idx = dir[str[0]]
        
        flag = 0
        x = start[0] 
        y = start[1]
        for i in range(int(str[1])):
            x += dx[idx]
            y += dy[idx]
            if x < 0 or x >= n or y < 0 or y >= m or park[x][y] == "X":
                flag = 1
                break
        if flag == 0:
            start[0] += dx[idx] * int(str[1])
            start[1] += dy[idx] * int(str[1])
            
    return start