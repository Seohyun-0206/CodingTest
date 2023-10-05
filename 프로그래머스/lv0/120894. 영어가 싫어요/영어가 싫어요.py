def solution(numbers):
    num_str = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    
    answer = 0
    for k, v in num_str.items():
        numbers = numbers.replace(k, v)
    return int(numbers)