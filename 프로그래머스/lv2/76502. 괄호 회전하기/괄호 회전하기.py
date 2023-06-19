from collections import deque

dt = {"{": "}", "[": "]", "(": ")"}

def solution(s):
    answer = 0
    tests = deque(s)

    for _ in range(len(s)):
        stack = []
        for test in tests:
            if test in dt:
                stack.append(dt[test])
            else:
                if stack and stack[-1] == test:
                    stack.pop()
                else:
                    stack.append(test)
        if not stack:
            answer += 1
        tests.rotate(-1)

    return answer