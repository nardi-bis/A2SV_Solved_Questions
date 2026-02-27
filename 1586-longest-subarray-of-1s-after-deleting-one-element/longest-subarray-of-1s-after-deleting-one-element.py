class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nz=0
        l=0
        res=0
        for r in range(len(nums)):
            if nums[r]==0:
                nz+=1
            while nz>1:
                if nums[l]==0:
                    nz-=1
                l+=1
            res=max(res,r-l)
        return res
