class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter()
        count[0] = 1
        runsum = 0
        res = 0

        for i in range(n):
            runsum += nums[i]
            remain = runsum % k
            res += count[remain]
            count[remain] += 1

        return res
            

