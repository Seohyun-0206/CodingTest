def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += i
            continue
        ch = ord(i) + n
        if ch > 122 and i.islower():
            ch -= 26
        elif ch > 90 and i.isupper():
            ch -= 26
        
        answer += chr(ch)
    return answer