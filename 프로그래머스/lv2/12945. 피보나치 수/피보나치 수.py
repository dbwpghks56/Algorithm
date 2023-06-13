import functools
import sys
sys.setrecursionlimit(500000)


dp = {}
@functools.lru_cache(maxsize=None)
def solution(n):
    if n == 1 or n == 2:
        return 1
    
    if n not in dp:
        dp[n] = solution(n-1) + solution(n-2)
        
    return dp[n] % 1234567
    
    
    
    
    
    