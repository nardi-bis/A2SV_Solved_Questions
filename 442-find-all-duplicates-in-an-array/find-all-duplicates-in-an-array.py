class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = nums[abs(num) - 1] * (-1)
            else:
                res.append(abs(num))
        return res

        