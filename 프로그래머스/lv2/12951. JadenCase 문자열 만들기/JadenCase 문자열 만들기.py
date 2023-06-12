def solution(s):
    answer = []
    test = s.split(" ")
    result = ""
    
    for t in test:
        answer.append(t.capitalize())
    
#     if s[-1]  == " ":
#         answer.append("")
        
#     if s[0] == " ":
#         answer.insert(0, "")
        
    result = " ".join(answer)
        
    return result





