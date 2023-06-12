from collections import deque

def solution(arr):
    answer = []
    asset = deque()
    for a in arr:
        if answer == []:
            answer.append(a)
            
        else:
            if answer[-1] != a:
                answer.append(a)
#         print(asset)
#         print(answer)
#         if len(asset) == 0:
#             asset.append(a)
            
#         else:
#             ast = asset.popleft()
#             if a == ast:
#                 answer.append(ast)
                
#             else:
#                 answer.append(ast)
#                 asset.append(a)
            
    return answer








