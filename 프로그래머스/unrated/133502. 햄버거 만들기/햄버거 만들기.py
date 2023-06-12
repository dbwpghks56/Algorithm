# def solution(ingredient):
#     answer = []
#     result = 0
    
#     for i in ingredient:
#         print(answer)
#         if answer == []:
#             if i == 1:
#                 answer.append(i)
        
#         else:
#             if i == 2:
#                 if answer.pop() == 1:
#                     answer.append(i)
                    
#             elif i == 3:
#                 if answer.pop() == 2:
#                     answer.append(i)
                    
#             elif i == 1:
#                 if answer[-1] == 3:
#                     answer.pop()
#                     result += 1
#                 else:
#                     answer.append(i)
                
#     return result
def solution(ingredient):
    answer = []
    result = 0

    for i in ingredient:
        answer.append(i)  # 재료를 일단 answer 리스트에 추가

        # answer 리스트의 길이가 4 이상인 경우에만 체크
        if len(answer) >= 4:
            if answer[-4:] == [1, 2, 3, 1]:
                answer.pop()  # 연속된 재료가 발견되면 마지막 요소를 제거
                answer.pop()  # 마지막에서 두 번째 요소 제거
                answer.pop()  # 마지막에서 세 번째 요소 제거
                answer.pop()  # 첫 번째 요소 제거
                result += 1

    return result







