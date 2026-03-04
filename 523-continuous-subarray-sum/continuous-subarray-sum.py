class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if the remainder of two prefix sum when divided by k is the same then subarray between them is divisible by k
        hashmap = {0:-1} # remainder, index
        runsum = 0
        for i, num in enumerate(nums):
            runsum += num
            remainder = runsum % k
            if remainder in hashmap:
                if i - hashmap[remainder] > 1:
                    return True
            else:
                hashmap[remainder] = i
        return False