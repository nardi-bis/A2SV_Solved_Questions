class Solution:
    def findErrorNums(self,nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        
        # Cycle sort
        while i < n:
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        # Find duplicate and missing
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]