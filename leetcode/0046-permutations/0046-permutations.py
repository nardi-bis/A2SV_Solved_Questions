class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def per (path):
            if  len(path)== len(nums):
                result.append(path[:])
                return 
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    per(path)
                    path.pop()
        per([])
        return result



        