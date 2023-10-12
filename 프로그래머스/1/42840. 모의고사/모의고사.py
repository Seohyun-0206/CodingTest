def solution(answers):
    correct = {1 : 0, 2 : 0, 3 : 0}
    
    n1 = 1
    n2 = 5
    n3 = 3
    for i in range(len(answers)):
        if n1 == answers[i]:
            correct[1] += 1
        if i % 2 == 0:
            n2 = number2(n2)
            if answers[i] == 2:
                correct[2] += 1
        elif n2 == answers[i]:
            correct[2] += 1
        if n3 == answers[i]:
            correct[3] += 1    
        
        n1 += 1
        if n1 > 5:
            n1 = 1
        if i % 2 != 0:
            n3 = number3(n3)
            
    correct = sorted(correct.items(), key=lambda x:x[1], reverse=True)
    answer = []
    for i in range(3):
        if correct[i][1] == correct[0][1]:
            answer.append(correct[i][0])
    return answer

    
def number2(n2):
    if n2 == 1: n2 = 3
    elif n2 == 5: n2 = 1
    else: n2 += 1
    
    return n2

def number3(n3):
    if n3 == 3: n3 = 1
    elif n3 == 1 or n3 == 4: n3 += 1
    elif n3 == 2: n3 = 4
    elif n3 == 5: n3 = 3
    
    return n3