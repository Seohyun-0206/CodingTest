def solution(id_pw, db):
    answer = 'fail'
    for id in db:
        if id == id_pw:
            answer = "login"
            break
        elif id[0] == id_pw[0]:
            answer = 'wrong pw'
    return answer