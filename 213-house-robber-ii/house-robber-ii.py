class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def dp(n, houses):
            if n == 0:
                return houses[0]
            if n == 1:
                return max(houses[0], houses[1])
            if (n, houses) not in memo:
                memo[(n, houses)] = max(dp(n - 1, houses), dp(n - 2, houses) + houses[n])
            return memo[(n, houses)]

        a, b = nums[:-1], nums[1:]
        return max(dp(len(a) - 1, tuple(a)), dp(len(b) - 1, tuple(b)))