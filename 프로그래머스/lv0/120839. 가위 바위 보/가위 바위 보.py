def solution(rsp):
    cases = {'2':'0', '0':'5', '5':'2'}
    answer = ''
    
    for i in rsp:
        answer += cases[i]
    return answer