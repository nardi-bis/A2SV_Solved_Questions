class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_ = 0
        for i in range(1, len(nums)):
            value = nums[i] - nums[i - 1]
            max_ = max(max_, value)
        return max_

             
        