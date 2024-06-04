from math import gcd

def solutino(N, M):
    answer = 0

    lcm = N*M//gcd(N, M)
    answer = lcm//M

    return answer