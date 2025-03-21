import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
ildan = []
juldae = []

for _ in range(n):
    m = int(sys.stdin.readline())

    if m != 0 :
        heappush(ildan, (abs(m), m))

    else:
        if len(ildan) == 0:
            print(0)
        else:
            print(heappop(ildan)[1])