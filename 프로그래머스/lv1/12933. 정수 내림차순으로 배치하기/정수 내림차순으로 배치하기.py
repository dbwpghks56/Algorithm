def solution(n):
    answer = []
    
    while n:
        d, m = divmod(n,10)
        n = d
        answer.append(m)
    answer.sort(reverse=True)
    
    return int(''.join(map(str, answer)))