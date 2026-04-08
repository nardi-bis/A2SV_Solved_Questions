class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right: # why not left >= right
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # minimum is in the right side
                left = mid + 1
            else:
                right = mid        
        return nums[left]

        