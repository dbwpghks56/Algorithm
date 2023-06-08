import sys

input = sys.stdin.readline

n, m = map(int, input().split())

while n % m != 0 :
    r = n % m
    n = m
    m = r
    
print("1" * m)