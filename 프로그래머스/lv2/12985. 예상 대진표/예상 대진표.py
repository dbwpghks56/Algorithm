def solution(n,a,b):
    answer = 0

    while(a!=b):
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
    #1   => 2
    #2   => 2
    #3   => 4
    #4   => 4

    return answer

    return answer