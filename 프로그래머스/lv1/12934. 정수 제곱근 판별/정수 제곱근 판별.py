import math

def solution(n):
    answer = 0
    
    sqrts = round(math.sqrt(n),2)
    
    if (sqrts % 1) == 0.0:
        answer = (sqrts + 1)**2
        
    else:
        answer = -1
    
    return answer