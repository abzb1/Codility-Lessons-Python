def solution(A):
    N = len(A)
    fib = [0, 1]
    while fib[-1] <= N + 1:
        fib.append(fib[-1] + fib[-2])

    reachable = [-1] * (N + 1)
    reachable[0] = 0

    queue = [0]

    while queue:
        pos = queue.pop(0)
        for jump in fib:
            next_pos = pos + jump
            if next_pos == N + 1:
                return reachable[pos] + 1
            if next_pos <= N and reachable[next_pos] == -1 and A[next_pos - 1] == 1:
                reachable[next_pos] = reachable[pos] + 1
                queue.append(next_pos)

    return -1