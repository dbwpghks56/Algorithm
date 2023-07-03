from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    dq = deque()
    
    for city in cities:
        city2 = city.casefold()
        if city2 in dq:
            dq.remove(city2)
            dq.append(city2)
            answer += 1
            
        else:
            answer += 5
            if len(dq) == cacheSize:
                dq.popleft()
            dq.append(city2)
    
    return answer