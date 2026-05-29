class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, x):
            if i >= len(prices):
                return 0

            n = (i, x)          
            if n not in memo:         
                if x:
                    sell = prices[i] + dp(i + 2, False)
                    hold = dp(i + 1, True)
                    memo[n] = max(sell, hold)
                else:
                    buy= -prices[i] + dp(i + 1, True)
                    skip = dp(i + 1, False)
                    memo[n] = max(buy, skip)
            return memo[n]

        return dp(0, False)


            