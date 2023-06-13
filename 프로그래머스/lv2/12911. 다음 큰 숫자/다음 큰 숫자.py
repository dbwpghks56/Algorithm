from collections import Counter

def solution(n):
    answer = n + 1
    binn = bin(n)[2:]
    onum = Counter(binn)["1"]
    while True:
        anum = Counter(bin(answer)[2:])["1"]
        if anum == onum:
            break
        else:
            answer += 1
        
    return answer