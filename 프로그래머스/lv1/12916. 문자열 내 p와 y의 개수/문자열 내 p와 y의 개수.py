def solution(s):
    answer = True
    pnum = 0
    ynum = 0
    
    for sn in s:
        if sn == "P" or sn =="p":
            pnum += 1
            
        if sn =="Y" or sn =="y":
            ynum += 1

    return True if (pnum == ynum) else False