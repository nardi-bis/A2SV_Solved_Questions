class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        runsum = 0
        for i in range(n):
            runsum += nums[i]
            nums[i] = runsum
        min_ = min(nums)
        if min_ < 0:
            min_ *= -1
            return min_ + 1 
        else: 
            return 1

        