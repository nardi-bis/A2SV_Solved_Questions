class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if the remainder of two prefix sum when divided by k is the same then subarray between them is divisible by k
        remainder_map = {0: -1}   # remainder : index
        runsum = 0

        for i, num in enumerate(nums):
            runsum += num
            remainder = runsum % k

            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i

        return False