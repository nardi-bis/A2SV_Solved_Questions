class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        l = len(nums)
        def dp(n):
            if n == 0:
                return nums[n]
            if n == 1:
                return max(nums[n - 1], nums[n])
            if n not in memo:
                memo[n] = max(nums[n] + dp(n - 2), dp(n - 1))
            return memo[n]
        return dp(l-1)

            
