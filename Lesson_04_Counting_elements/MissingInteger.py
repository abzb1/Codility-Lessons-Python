def solution(A):
    answer = 1
    A.sort()
    for a in A:
        if a == answer:
            answer += 1
        elif a > answer:
            break
    
    return answer