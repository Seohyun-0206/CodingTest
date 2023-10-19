def solution(s):
    answer = []
    word = list(s.split(" "))
    for w in word:
        str = ''
        for i in range(len(w)):
            if i % 2 == 0:
                str += w[i].upper()
            else:
                str += w[i].lower()
        answer.append(str)
    return ' '.join(answer)