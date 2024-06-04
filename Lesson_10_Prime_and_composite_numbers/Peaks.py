def solution(A):
    answer = 0
    N = len(A)
    peaks = [i for i in range(1, N-1) if A[i-1] < A[i] > A[i+1]]
    if not peaks:
        return answer

    for block_count in reversed(range(1,len(peaks)+1)):
        if N%block_count == 0:
            block_size = N//block_count
            block_with_peak = set()
            for peak in peaks:
                block_with_peak.add(peak//block_size)
            if len(block_with_peak) == block_count:
                answer = block_count
                return answer

    return answer