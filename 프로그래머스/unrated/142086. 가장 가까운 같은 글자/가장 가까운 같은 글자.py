from collections import deque

def solution(s):
    answer = []
    stack = []
    
    for ss in s:
        count = 0
        idx = 0
        if stack == []:
            answer.append(-1)
            stack.append(ss)
            
        else:
            answer.append(-1)
            
            if ss in stack:
                while True:
                    idx -= 1
                    count += 1
                    answer[-1] = count
                    
                    if stack[idx] == ss or idx == 0:
                        break
                
            stack.append(ss)
    
    
    return answer