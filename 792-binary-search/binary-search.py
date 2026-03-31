class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            sums = left + right
            if nums[sums//2] == target:
                return sums//2
            elif nums[sums//2] < target:
                left = sums//2 + 1
            else:
                right = sums//2 - 1
        return -1


        