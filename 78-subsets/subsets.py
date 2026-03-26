class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(start, path):
            ans.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                back(i+1,path)
                path.pop()
        back(0, [])
        return ans