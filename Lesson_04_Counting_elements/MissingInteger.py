from collections import Counter

def solution(A):
    answer = 0
    cnt_A = Counter(A)
    max_A = max(A)
    for i in range(1, max(2,max_A+1)+1):
        if i in cnt_A:
            continue
        else:
            answer = i
            break

    return answer