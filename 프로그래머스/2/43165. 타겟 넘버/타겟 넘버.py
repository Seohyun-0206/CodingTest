def solution(numbers, target):
    answer = 0
    visited = [0]
    
    for n in numbers:
        tmp = []
        for v in visited:
            tmp.append(v + n)
            tmp.append(v - n)
        visited = tmp
    
    return visited.count(target)
