def solution(A):
    answer = 0

    left = sorted([i-r for i,r in enumerate(A)])
    right = sorted([i+r for i,r in enumerate(A)])

    active_discs = 0
    idx_left = 0
    
    N = len(A)
    for idx_right in range(N):
        while idx_left < N and left[idx_left] <= right[idx_right]:
            answer += active_discs
            if answer > 10000000:
                return -1
            active_discs += 1
            idx_left += 1
        active_discs -= 1

    return answer