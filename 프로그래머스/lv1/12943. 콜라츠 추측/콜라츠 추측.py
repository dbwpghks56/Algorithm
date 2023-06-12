def solution(num):
    return ifOdd(num, 0)

def ifOdd(num, i):
    if num == 1:
        return i
    
    elif i >= 500:
        return -1
    
    else:
        i += 1
        if num % 2 == 0:
            return ifOdd(num/2, i)
            
        else:
            return ifOdd((num * 3) +1, i)





