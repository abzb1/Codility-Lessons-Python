from collections import Counter

def solution(A):
    answer = 0

    cnt = Counter(A)
    for k, v in cnt.items():
        if v%2==1:
            answer = k
            break

    return answer