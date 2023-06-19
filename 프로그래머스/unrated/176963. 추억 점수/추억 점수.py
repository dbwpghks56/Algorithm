def solution(name, yearning, photo):
    answer = [] 
    dt = {}
    
    for i in range(len(name)):
        dt[name[i]] = yearning[i]
        
    for p in range(len(photo)):
        a = 0
        for s in photo[p]:
            if s in dt:
                a += dt[s]
                
        answer.append(a)
    
    return answer