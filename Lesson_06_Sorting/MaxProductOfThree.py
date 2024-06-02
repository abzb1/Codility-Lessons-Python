def solution(A):
    answer = 0
    A.sort(reverse=True)
    pos = [a for a in A if a>=0]
    neg = [a for a in reversed(A) if a<0]
    
    if len(neg)>=2:
        if len(pos)>=1:
            neg_neg_pos = neg[0]*neg[1]*pos[0]
            max_max_max = A[0]*A[1]*A[2]
            answer = max(neg_neg_pos, max_max_max)
        else:
            answer = A[0]*A[1]*A[2]
    else:
        answer = A[0]*A[1]*A[2]

    return answer