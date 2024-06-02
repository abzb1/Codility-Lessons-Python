def solution(X, A):
    answer = -1
    fallen = set()
    
    for i, a in enumerate(A):
        fallen.add(a)
        if len(fallen) == X:
            answer = i
            break

    return answer