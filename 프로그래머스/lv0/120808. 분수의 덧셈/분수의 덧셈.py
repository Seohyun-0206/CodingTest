import math
def solution(numer1, denom1, numer2, denom2):
    x = denom1 * denom2 // math.gcd(denom1, denom2)
    x1 = x // denom1
    x2 = x // denom2
    answer = [numer1 * x1 + numer2 * x2, x]
    y = math.gcd(answer[0], answer[1])
    return [answer[0] // y, answer[1] // y]