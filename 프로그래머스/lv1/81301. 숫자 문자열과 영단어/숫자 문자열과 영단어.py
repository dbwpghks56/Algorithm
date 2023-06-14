def solution(s):
    dt = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }
    
    
    for val in dt:
        s = s.replace(val, str(dt[val]))
    
    return int(s)










