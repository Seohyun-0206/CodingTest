import math
def solution(numer1, denom1, numer2, denom2):
    numer = denom2 * numer1 + denom1 * numer2
    denom = denom1 * denom2
    gcd = math.gcd(numer, denom)
    return [numer // gcd, denom // gcd]