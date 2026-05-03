class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, res, upto = 0, 0, 0
        N = len(nums)
        
        while upto < n:
            if i < N and nums[i] <= upto + 1:
                upto += nums[i]
                i += 1
            else:
                res += 1
                upto += (upto + 1)
        return res

        