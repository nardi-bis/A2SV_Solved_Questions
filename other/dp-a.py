import sys
sys.setrecursionlimit(200000)
n = int(input())
h = list(map(int, input().split()))
    
memo = {}
    
def dp(i):
    if i == 0:
        return 0
    if i not in memo:
        memo[i] = dp(i - 1)  + abs(h[i] - h[i - 1])
        if i >=2:
            memo[i] = min(memo[i], dp(i-2) + abs(h[i] - h[i-2])) 
    return memo[i]
print(dp(n - 1))