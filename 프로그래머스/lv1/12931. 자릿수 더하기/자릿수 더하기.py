def solution(n):
    answer = 0

    while n:
        d,m = divmod(n, 10)
        answer += m
        n = d

    return answer