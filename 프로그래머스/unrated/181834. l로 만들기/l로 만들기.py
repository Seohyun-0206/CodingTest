def solution(myString):
    answer = ["l" if i < "l" else i for i in myString]
    return "".join(answer)