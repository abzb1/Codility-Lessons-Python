def solution(H):
    answer = 0
    stack = []

    for height in H:
        while stack and stack[-1] > height:
            stack.pop()
            answer += 1

        if not stack or stack[-1] < height:
            stack.append(height)

    answer += len(stack)
    return answer