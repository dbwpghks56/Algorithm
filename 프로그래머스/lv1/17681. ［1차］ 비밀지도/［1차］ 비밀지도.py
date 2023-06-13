from collections import deque

def solution(n, arr1, arr2):
    answer = []

    for idx, val in enumerate(arr1):
        arr1[idx] = bin(val)[2:]

    for idx, val in enumerate(arr2):
        arr2[idx] = bin(val)[2:]

    for i in range(n):
        # 이진수로 변환된 값을 정수로 변환
        num1 = int(arr1[i], 2)
        num2 = int(arr2[i], 2)
        # 정수들을 비트 단위로 or 연산하여 이진수로 변환
        result = bin(num1 | num2)[2:]
        # 결과를 0으로 채워진 문자열로 조정
        result = result.zfill(n)
        answer.append(result)
        
    for idx, val in enumerate(answer):
        answer[idx] = val.replace("1","#")
        
        
    for idx, val in enumerate(answer):
        answer[idx] = val.replace("0"," ")
    
    return answer