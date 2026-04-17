class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1

        for num in nums:
            if num < ans:
                continue
            elif num == ans:
                ans += 1
            else:
                return ans

        return ans