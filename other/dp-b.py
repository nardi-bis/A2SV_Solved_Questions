import sys
sys.setrecursionlimit(200000)
n, k = map(int, input().split())
h = list(map(int, input().split()))

memo = {}
def dp(i):
    if i == 0:
        return 0
    if i not in memo:
        memo[i] = dp(i - 1) + abs(h[i] - h[i - 1])
        for j in range(2, k + 1):
            if i - j >= 0:
                memo[i] = min(memo[i], dp(i - j) + abs(h[i] - h[i - j]))
    return memo[i]
print(dp(n - 1))