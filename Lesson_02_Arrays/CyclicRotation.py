def solution(A, K):
    if len(A)==0:
        return A
    K = K%len(A)
    A = A[len(A)-K:]+A[:len(A)-K]
    
    return A