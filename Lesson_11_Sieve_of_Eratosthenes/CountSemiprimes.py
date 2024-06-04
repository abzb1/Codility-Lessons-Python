def solution(N, P, Q):
    answer = []

    sieve = [False]*2 + [True for _ in range(N-1)]
    for i in range(int((N+1)**0.5)+1):
        if sieve[i]:
            for j in range(i, N+1, i):
                if j>i:
                    sieve[j] = False
    primes = [i for i in range(N+1) if sieve[i]]
    semi_cnt = [0 for _ in range(N+1)]
    for p in primes:
        for i in range(p, N+1, p):
            num = i
            while num%p==0:
                semi_cnt[i] += 1
                num = num//p

    ps_semi_primes = [0 for _ in range(N+1)]
    for i in range(N):
        if semi_cnt[i+1]==2:
            ps_semi_primes[i+1] = ps_semi_primes[i] + 1
        else:
            ps_semi_primes[i+1] = ps_semi_primes[i]

    for p, q in zip(P, Q):        
        cnt = ps_semi_primes[q]-ps_semi_primes[p-1]
        answer.append(cnt)

    return answer