import sys

a, b = sys.stdin.readline().split()

min_diff = 51

# B에서 A와 같은 길이의 부분 문자열을 순회하면서 최소 차이 찾기
for i in range(len(b) - len(a) + 1):
    diff = 0
    sub_b = b[i:i+len(a)]  # B에서 A와 같은 길이의 부분 문자열 추출
    for x, y in zip(a, sub_b):
        if x != y:
            diff += 1
    min_diff = min(min_diff, diff)  # 최소 차이 갱신

# 결과 출력
print(min_diff)
