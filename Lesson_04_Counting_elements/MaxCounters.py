def solution(N, A):
    cnts = [0 for _ in range(N)]
    max_counter = 0
    last_update = 0

    for a in A:
        if a <= N:
            cnts[a-1] = max(cnts[a-1], last_update) + 1
            max_counter = max(max_counter, cnts[a-1])
        else:
            last_update = max_counter

    for i in range(N):
        cnts[i] = max(cnts[i], last_update)

    return cnts