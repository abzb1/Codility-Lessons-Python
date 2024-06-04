from math import ceil

def solution(N):
    answer = 0

    for i in range(1, ceil((N+1)**0.5)):
        if N%i == 0:
            if N//i == i:
                answer += 1
            else:
                answer += 2

    return answer