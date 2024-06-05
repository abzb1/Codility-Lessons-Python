def solution(K, A):
    answer = 0

    tied = 0
    for a in A:
        tied += a
        if tied >= K:
            answer += 1
            tied = 0
            
    return answer