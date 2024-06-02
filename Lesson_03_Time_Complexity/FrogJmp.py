from math import ceil

def solution(X, Y, D):
    answer = 0

    length = Y-X
    answer = ceil(length/D)

    return answer