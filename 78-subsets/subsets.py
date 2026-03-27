class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def back(i):
            if i >= len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[i])
            back(i+1)

            subset.pop()
            back(i+1)

          
        back(0)
        return ans