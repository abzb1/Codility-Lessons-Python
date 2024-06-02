def solution(S):
    
    stack = []
    for s in S:
        if s=="(":
            stack.append(1)
        elif s==")":
            if stack:
                stack.pop(-1)
            else:
                return 0
    
    if stack:
        return 0
    
    return 1