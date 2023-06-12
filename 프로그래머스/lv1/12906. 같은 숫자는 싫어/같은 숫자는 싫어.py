def solution(arr):
    answer = []
    for a in arr:
        if answer == []:
            answer.append(a)
            
        else:
            if answer[-1] != a:
                answer.append(a)
         
    return answer








