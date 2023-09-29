def solution(numbers, direction):
    if direction == "right":
        x = numbers.pop()
        numbers.insert(0, x)
    elif direction == "left":
        x = numbers[0]
        del numbers[0]
        numbers.append(x)
        
    return numbers