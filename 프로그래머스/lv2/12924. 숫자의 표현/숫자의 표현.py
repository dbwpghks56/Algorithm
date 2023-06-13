def solution(n):
    answer = [0]
    result = 0
    
    for i in range(1, n):
        answer.append(answer[-1] + i)
        
    prev = 0
    nex = 1
    print(answer)
    while prev < len(answer):
        if nex < len(answer):
            if (answer[nex] - answer[prev]) > n:
                prev += 1
                
            elif(answer[nex] - answer[prev]) < n:
                nex += 1
                
            elif (answer[nex] - answer[prev]) == n :
                result +=1
                prev += 1
                nex = prev + 1
            
        else:
            prev += 1
            nex = prev + 1

    return result + 1









