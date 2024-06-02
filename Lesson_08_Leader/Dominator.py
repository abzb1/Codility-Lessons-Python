from collections import Counter
from math import floor

def solution(A):
    if len(A) == 0:
        return -1
    cnt_A = Counter(A)
    dom = 0
    dom_num = 0
    for k, v in cnt_A.items():
        if v >= dom_num:
            dom = k
            dom_num = v
    
    if dom_num <= floor(len(A)/2):
        return -1
    
    answer = A.index(dom)

    return answer