from collections import deque
def solution(priorities, location):
    answer = 0
    
    pro = deque([i for i in range(len(priorities))])
    
    while len(pro) > 0:
        p = pro.popleft()
        if priorities[p] < max(priorities):
            pro.append(p)
        else:
            priorities[p] = -1
            answer += 1
            if p == location:
                return answer

    return answer