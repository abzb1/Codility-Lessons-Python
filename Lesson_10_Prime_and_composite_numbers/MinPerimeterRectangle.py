from math import ceil

def solution(N):
    answer = 0
    
    for i in reversed(range(1, ceil((N+1)**0.5))):
        if N%i==0:
            answer = 2*(i+N//i)
            break

    return answer