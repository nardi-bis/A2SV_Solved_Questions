class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = (10**9 +7)   
        cost = 0
        nums = []
        for x in instructions:
            smaller = bisect_left(nums, x)
            greater = len(nums) - bisect_right(nums, x)
            cost += min(smaller, greater)
            insort(nums, x)
        return cost % mod