from math import gcd

def solution(A, B):
    answer = 0
    
    for a, b in zip(A, B):
        gcd_ab = gcd(a, b)
        gcd_a = 0
        gcd_b = 0
        while gcd_a != 1:
            gcd_a = gcd(a, gcd_ab)
            a //= gcd_a
        while gcd_b != 1:
            gcd_b = gcd(b, gcd_ab)
            b //= gcd_b
        if a == b:
            answer += 1

    return answer