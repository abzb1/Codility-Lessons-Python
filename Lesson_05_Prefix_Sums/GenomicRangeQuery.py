def solution(S, P, Q):
    answer = []

    prefix_sums = {"A": [0 for _ in range(len(S)+1)],
                   "C": [0 for _ in range(len(S)+1)],
                   "G": [0 for _ in range(len(S)+1)],
                   "T": [0 for _ in range(len(S)+1)],}
    
    for i, s in enumerate(S):
        for k in prefix_sums:
            prefix_sums[k][i+1] = prefix_sums[k][i] + (s==k)

    ifs = {"A": 1,
           "C": 2,
           "G": 3,
           "T": 4}

    for p, q in zip(P, Q):
        for k in prefix_sums:
            if prefix_sums[k][q+1]-prefix_sums[k][p] > 0:
                answer.append(ifs[k])
                break

    return answer