def solution(A):
    answer = 0
    peaks = [i for i in range(1, len(A)-1) if A[i-1] < A[i] > A[i+1]]
    if len(peaks) < 2:
        answer = len(peaks)
        return answer

    answer = 1
    for flags in range(2, len(peaks)+1):
        last_flag, count = -flags, 0
        for peak in peaks:
            if peak-last_flag >= flags:
                count += 1
                last_flag = peak
                if count == flags:
                    break
        if count < flags:
            break
        answer = flags

    return answer