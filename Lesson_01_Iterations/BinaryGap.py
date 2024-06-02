def solution(N):
    answer = 0
    bin_N = bin(N).lstrip("0b")

    consect_zero = 0
    for b in bin_N:
        if b=="1":
            answer = max(answer, consect_zero)
            consect_zero = 0
        else:
            consect_zero += 1

    return answer