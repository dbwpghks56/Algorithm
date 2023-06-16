import math

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = lcm_calculation(lcm, arr[i])
    return lcm

def lcm_calculation(a, b):
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    return lcm