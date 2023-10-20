def solution(s):
    words = list(s.lower())
    for i in range(len(words)):
        if i == 0 and words[i] != ' ':
            words[i] = words[i].upper()
        if i > 0 and words[i - 1] == ' ':
            words[i] = words[i].upper()

    return ''.join(words)