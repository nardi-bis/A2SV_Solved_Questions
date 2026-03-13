class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0

        for x in nums:
            if count < 0:
                return False
            elif x > count:
                count = x
            count = count - 1
        return True




        