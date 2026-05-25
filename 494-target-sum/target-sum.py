class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, current_sum):
            n = (i, current_sum)        

            if n not in memo:
                if i == len(nums):
                    memo[n] = 1 if current_sum == target else 0
                else:
                    memo[n] = (dp(i + 1, current_sum + nums[i]) +
                            dp(i + 1, current_sum - nums[i]))
            return memo[n]
        return dp(0, 0)
        