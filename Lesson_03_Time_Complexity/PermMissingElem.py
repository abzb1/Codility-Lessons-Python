def solution(A):
    answer = 0
    A.sort()
    if len(A)==0:
        answer = 1
    for i, a in enumerate(A):
        if (i+1)!=a:
            answer = i+1
            break
        if i==len(A)-1:
            answer = i+2

    return answer