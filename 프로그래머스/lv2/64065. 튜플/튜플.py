from collections import Counter

def solution(s):
    answer = []
    ss = ''.join(list(s.split("{")))
    sss = ''.join(list(ss.split("}")))
    ssss = list(sss.split(","))
    counter = Counter(ssss)
    most_common = counter.most_common()
    
    for item in most_common:
        answer.append(int(item[0]))
    
    return answer