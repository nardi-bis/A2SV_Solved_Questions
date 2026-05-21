class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(x):
            if x == 0:
                return 0
            if x <= 2:
                return 1
            if x not in memo:
                d = x - 3
                memo[x] = dp(d) + dp(d + 1) + dp(d + 2)
            return memo[x]
        return dp(n)
