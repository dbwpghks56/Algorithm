def solution(n):
    answer = 0
    
    for i in range(n):
        if (n % (i + 1)) == 1:
            if answer == 0:
                answer = i+1
            else:
                anwer = min(answer, i+1)
    return answer