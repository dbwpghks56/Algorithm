def solution(brown, yellow):
    answer = []
    wholelist = []
    whole = brown + yellow
    
    for i in range(1, whole+1):
        if whole % i == 0:
            wholelist.append(i)
    print(wholelist)
    print(len(wholelist))
    maxs = len(wholelist) -1
    for idx in range(maxs, -1, -1):
        row = wholelist[idx]
        col = wholelist[maxs-idx]
        
        if (row + (col -1) + (row -1) + (col - 2) == brown):
            return [row, col]
        
    return answer






