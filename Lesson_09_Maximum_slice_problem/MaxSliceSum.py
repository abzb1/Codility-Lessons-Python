def solution(A):
    
    answer = A[0]
    max_ending = A[0]
    for i in range(1,len(A)):
        max_ending = max(A[i], max_ending + A[i])
        answer = max(answer, max_ending)

    return answer