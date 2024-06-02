def solution(S):
    
    bras = ["(","{","[",]
    kets = [")","}","]",]
    
    stack = []
    for s in S:
        if s in bras:
            stack.append(s)
        elif s in kets:
            if stack:
                if stack[-1] == bras[kets.index(s)]:
                    stack.pop(-1)
                else:
                    return 0
            else:
                return 0

    if stack:
        return 0

    return 1