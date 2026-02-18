class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        m={}
        r=[]
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]]=i
        for i in range(len(nums)):
            r.append(m[nums[i]])
        return r

