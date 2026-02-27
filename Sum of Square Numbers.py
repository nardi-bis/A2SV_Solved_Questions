class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = [i for i in range(math.isqrt(c)+1)]
        l = 0
        r = len(nums) - 1
        while l <= r:
            total = nums[l] * nums[l] + nums[r] * nums[r]

            if total == c:
                return True
            elif total < c:
                l += 1
            else:
                r -= 1

        return False
              
        
