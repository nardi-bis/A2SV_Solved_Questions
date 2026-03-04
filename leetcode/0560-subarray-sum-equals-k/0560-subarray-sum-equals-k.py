class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        result = 0
        current_sum = 0
        prefixsums = { 0 : 1 }
        for n in nums:
            current_sum += n
            diff = current_sum - k
            result += prefixsums.get(diff, 0)
            prefixsums[current_sum] = 1 + prefixsums.get(current_sum, 0)
        return result


       


        