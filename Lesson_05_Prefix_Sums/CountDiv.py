from math import ceil

def solution(A, B, K):
    answer = 0

    first_divisible = ceil(A/K)*K
    if first_divisible <= B:
        answer += 1
    answer += max(0,(B-first_divisible)//K)

    return answer