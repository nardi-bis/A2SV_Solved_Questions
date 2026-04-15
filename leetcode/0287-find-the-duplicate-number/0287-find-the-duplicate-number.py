class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        dup = -1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
        return dup  
        