def solution(x):
    answer = True
    test = 0
    n = x
    while n:
        d,m = divmod(n, 10)
        n = d
        test += m
    
    
    return True if (x%test) == 0 else False