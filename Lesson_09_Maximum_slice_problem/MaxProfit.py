def solution(A):
    answer = 0
    
    if not A:
        return answer
        
    min_price = A[0]
    for a in A:
        min_price = min(min_price, a)
        answer = max(answer, a-min_price)

    return answer