def solution(A):
    min_avg = float('inf')
    min_start_idx = 0

    for i in range(len(A) - 1):
        current_avg = (A[i] + A[i + 1]) / 2.0
        if current_avg < min_avg:
            min_avg = current_avg
            min_start_idx = i

        if i < len(A) - 2:
            current_avg = (A[i] + A[i + 1] + A[i + 2]) / 3.0
            if current_avg < min_avg:
                min_avg = current_avg
                min_start_idx = i

    return min_start_idx