def solution(n, words):
    answer = []
    stack = []
    dt = {}
    for i in range(n):
        dt[i] = []
    
    for idx, val in enumerate(words):
        if stack == []:
            dt[idx % n].append(val)
            stack.append(val)
            
        else:
            if val in stack:
                return [(idx % n) + 1, len(dt[idx % n]) + 1]
            
            if stack[-1][-1] == val[0]:
                stack.append(val)
                dt[idx % n].append(val)
            else:
                print(dt)
                print(stack)
                return [(idx % n) + 1, len(dt[idx % n]) + 1]

    print(dt)
    print(stack)
    return [0,0]