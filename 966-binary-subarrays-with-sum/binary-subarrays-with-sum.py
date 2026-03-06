class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count = Counter()
        count[0] = 1
        
        runsum = 0
        res = 0
        
        for num in nums:
            runsum += num
            res += count[runsum - goal]
            count[runsum] += 1
            
        return res
        
      