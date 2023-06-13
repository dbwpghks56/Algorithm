from collections import Counter

def solution(s):
    return jegui(s)

def jegui(s):
    if s == "":
        return 1
    
    answer = []
    
    for ss in s:
        if answer == []:
            answer.append(ss)
            
        else:
            if answer[-1] == ss:
                answer.pop()
                
            else:
                answer.append(ss)
                
    result = ''.join(answer)
    return 0 if result == s else jegui(result)
            
            
            
            
            
            
            
            
            