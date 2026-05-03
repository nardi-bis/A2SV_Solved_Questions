class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        split = 0
        right = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > right:
                parts = math.ceil(nums[i]/right)
                split += parts - 1
                right = nums[i] // parts
            else:
                right = nums[i]
        return split
    
         