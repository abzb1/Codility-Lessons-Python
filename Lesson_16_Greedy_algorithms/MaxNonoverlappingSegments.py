def solution(A, B):
    answer = 0
    end = -1
    for a, b in zip(A, B):
       if a > end:
           answer += 1
           end = b
           
    return answer