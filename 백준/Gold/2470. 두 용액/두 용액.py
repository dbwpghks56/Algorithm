import sys

n = int(sys.stdin.readline())
first = list(map(int, sys.stdin.readline().split()))  

first.sort()  # 정렬 필수!

left = 0
right = n - 1
answer = [first[left], first[right]]  # 초기값 설정
result = abs(first[left] + first[right])  # 초기 합 절댓값

while left < right:
    total = first[left] + first[right]  # 현재 합 계산

    # 더 0에 가까운 값이 나오면 업데이트
    if abs(total) < result:
        result = abs(total)
        answer = [first[left], first[right]]  # 더 가까운 쌍 저장

    # 0에 더 가까워지도록 포인터 이동
    if total < 0:
        left += 1
    else:
        right -= 1

# 항상 오름차순으로 출력
print(min(answer), max(answer))
