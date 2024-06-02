def solution(A):
    answer = 0
    cnt_zero = 0

    for a in A:
        if a == 0:
            cnt_zero += 1
        else:
            answer += cnt_zero
        if answer > 1_000_000_000:
            answer = -1
            break

    return answer