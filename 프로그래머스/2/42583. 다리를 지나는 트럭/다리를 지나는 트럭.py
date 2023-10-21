from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    b = deque([0] * bridge_length)
    truck = deque(truck_weights)
    cur = 0
    while len(truck) > 0:
        cur -= b.popleft()
        answer += 1
        if cur + truck[0] <= weight:
            t = truck.popleft()
            cur += t
            b.append(t)
        else:
            b.append(0)
    return answer + bridge_length