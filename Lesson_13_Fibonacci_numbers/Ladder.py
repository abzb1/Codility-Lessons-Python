def solution(A, B):
    max_rungs = max(A)  # Find the maximum number of rungs we need to calculate for
    
    # Fibonacci-like sequence with modulo calculations
    fib = [0] * (max(3, max_rungs + 1))  # Store results for each rung
    fib[1] = 1
    fib[2] = 2
    
    for i in range(3, max_rungs + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % (2**30)  # Optimized modulo calculation

    # Prepare the results
    results = [fib[rungs] % (2**power) for rungs, power in zip(A, B)]
    return results