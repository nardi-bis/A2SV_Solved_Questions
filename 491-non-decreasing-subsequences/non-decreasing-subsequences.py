class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(start, path):
            if len(path) >= 2 and path not in ans:
                ans.append(path[:])
            for i in range(start, len(nums)):
                if path and path[-1] > nums[i]:
                    continue
                path.append(nums[i])
                back(i+1, path)
                path.pop()
        back(0, [])
        return ans

