class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runsum = 0
        min_ = 0
        for n in nums:
            runsum += n
            min_ = min(min_, runsum)
        if min_ < 0:
            return 1 - min_
        else:
            return 1
        