from collections import Counter

def solution(A):
    cnt_A = Counter(A)
    max_A = max(A)
    
    if len(cnt_A) < max_A:
        return 0
    if sum(cnt_A.values()) > max_A:
        return 0
    
    return 1