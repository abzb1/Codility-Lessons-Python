def solution(A):
    answer = 0

    N = len(A)
    ends_left = [0 for _ in range(N)]
    ends_right = [0 for _ in range(N)]

    for i in range(1, N-1):
        ends_left[i] = max(0, ends_left[i-1] + A[i])
    for i in range(N-2, 0, -1):
        ends_right[i] = max(0, ends_right[i+1] + A[i])

    for i in range(1, N - 1):
        answer = max(answer, ends_left[i-1] + ends_right[i+1])

    return answer