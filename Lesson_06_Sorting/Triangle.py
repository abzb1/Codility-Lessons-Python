def solution(A):
    answer = 0

    def is_triangular(p, q, r):
        if p+q <= r:
            return 0
        elif q+r <= p:
            return 0
        elif r+p <= q:
            return 0
        return 1
    
    A.sort()

    for i in range(len(A)):
        if i+2 > len(A)-1:
            break

        p, q, r = A[i], A[i+1], A[i+2]
        if is_triangular(p, q, r):
            answer = 1
            break

    return answer