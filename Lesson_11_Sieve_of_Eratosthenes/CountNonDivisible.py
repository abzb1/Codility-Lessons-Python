from collections import Counter

def solution(A):
    answer = []

    cnt_A = Counter(A)
    num_nondivs = {k: len(A) for k in cnt_A}

    lst_A = list(sorted(cnt_A))
    max_A = lst_A[-1]
    for num1 in lst_A:
        for num2 in range(num1, max_A+1, num1):
            if num2 in cnt_A:
                if num2%num1 == 0:
                    num_nondivs[num2] -= cnt_A[num1]
    
    for a in A:
        answer.append(num_nondivs[a])
    
    return answer