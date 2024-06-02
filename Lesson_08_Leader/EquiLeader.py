from collections import Counter

def solution(A):
    N = len(A)
    counter = Counter(A)
    leader, cnt_leader = counter.most_common(1)[0]
    if cnt_leader <= N // 2:
        return 0

    equi_leaders = cnt_left = 0
    for i, num in enumerate(A[:-1]):
        cnt_left += num == leader
        left_half = cnt_left > (i+1) // 2
        right_half = (cnt_leader-cnt_left) > (len(A)-i-1) // 2
        equi_leaders += left_half and right_half

    return equi_leaders