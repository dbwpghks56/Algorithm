def solution(s):
    answer = [0,0]
    znum = 0
    bnum = 0
    
    print(go(s,answer,znum,bnum))
    return answer

def go(s,answer, znum, bnum):
    if s == "1":
        return answer
    
    test = ""
    for ss in s:
        if ss == "1":
            test += ss
        else:
            znum += 1
    bnum += 1
    answer[0] = bnum
    answer[1] = znum
    return go(bin(len(test))[2:], answer,znum,bnum)




