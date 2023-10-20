from collections import deque
def solution(s):
    q = deque()

    for x in s:
        if x == '(':
            q.append(x)
        elif x == ')':
            if not q:
                return False
            q.pop()
    
    if q:
        return False
    
    return True