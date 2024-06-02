def solution(A, B):
    answer = 0
    upstream_stack = []

    for size, direction in zip(A, B):
        if direction == 1:
            upstream_stack.append(size)
        else:
            while upstream_stack: 
                if upstream_stack[-1] < size:
                    upstream_stack.pop()
                else:
                    break
            else:
                answer += 1

    answer += len(upstream_stack)
    return answer