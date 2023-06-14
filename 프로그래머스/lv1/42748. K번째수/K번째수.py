def solution(array, commands):
    answer = []
    result = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        
        for s in range(i-1, j):
            answer.append(array[s])
            
        answer.sort()
        result.append(answer[k-1])
        answer = []
    
    return result