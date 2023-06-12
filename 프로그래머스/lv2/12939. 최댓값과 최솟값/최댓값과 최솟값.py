def solution(s):
    answer = ''
    test = list(map(int, s.split()))
    answer += str(min(test)) + " "
    answer += str(max(test))
    
    return answer