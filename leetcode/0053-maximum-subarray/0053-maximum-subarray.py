class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        cursum = 0
        for num in nums:
            if cursum < 0:
                cursum = 0
            cursum += num
            max_ = max(max_,cursum)
        return max_
        