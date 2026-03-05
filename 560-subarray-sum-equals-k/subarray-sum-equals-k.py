class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0] = 1
        runsum = 0
        ans = 0
        
        for num in nums:
            runsum += num

            ans += count[runsum - k]

            # if multiple starting point for the subarray exists
            if runsum in count:
                count[runsum] +=1
            else:
                count[runsum] = 1

            # count[runsum] += 1
            
        return ans
