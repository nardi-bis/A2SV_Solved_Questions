class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        c = Counter(nums)
        for k, v in c.items():
            if v == 2:
                res.append(k)
        for i in range(len(nums)):
            if i + 1 not in nums:
                res.append(i + 1)
                break
        return res


            
        