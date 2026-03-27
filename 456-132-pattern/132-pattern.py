class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        two = float("-inf")
        stack = []

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < two:
                return True
            while stack and nums[i] > stack[-1] :
                two =stack.pop()
            stack.append(nums[i])
        
        return False
            
