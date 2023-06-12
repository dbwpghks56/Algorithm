def solution(s):
    answer = True
    test = []
    
    for ss in s:
        if ss == "(":
            test.append(")")
            
        else:
            if test == []:
                return False
            test.pop()

    return True if test == [] else False