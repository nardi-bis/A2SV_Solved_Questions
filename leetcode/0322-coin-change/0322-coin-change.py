class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            if n not in memo:
                min_coins = amount + 1
                for coin in coins:
                    result = dp(n - coin)
                    if result != -1:
                        min_coins = min(min_coins, result + 1)
                if min_coins == amount + 1:
                    memo[n] = -1
                else:
                    memo[n] = min_coins

            return memo[n]

        return dp(amount)