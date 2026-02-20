class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        r=[]
        n=len(nums)//3
        c=Counter(nums)
        for num in c:
            if c[num]>n:
                r.append(num)
        return r
