from math import inf

def solution(A):
    answer = inf

    left_sum = 0
    right_sum = sum(A)
    for i in range(len(A)-1):
        a = A[i]
        left_sum+=a
        right_sum-=a
        diff = abs(left_sum-right_sum)
        answer = min(diff, answer)
    
    return answer