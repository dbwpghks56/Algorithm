def solution(a, b, n):
    answer = 0

    while int(n / a) != 0:
        s = n % a
        n /= a
        n = int(n)
        answer += (n * b)
        n = (n * b)
        if s != 0:
            n += s
        
        # print(answer)
    
    return answer