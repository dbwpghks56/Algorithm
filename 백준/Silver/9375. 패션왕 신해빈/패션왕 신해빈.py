import sys

n = int(sys.stdin.readline())

for _ in range(n):
    first = {}
    mola = {}
    m = int(sys.stdin.readline())
    for _ in range(m):
        fit = sys.stdin.readline().split()
        if fit[1] in first:
                first[fit[1]].append(fit[0])
        else:
            first[fit[1]] = [fit[0]]

    if len(first.keys()) == 1:
        print(m)

    else:
        count = 1
        for key in first:
            count *= (len(first[key]) + 1)  # 선택하지 않는 경우 포함
        print(count - 1)
