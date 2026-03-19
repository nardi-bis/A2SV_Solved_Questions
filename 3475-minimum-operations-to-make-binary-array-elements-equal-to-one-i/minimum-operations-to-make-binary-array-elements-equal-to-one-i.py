class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i + 2 >= len(nums): # cannot flip if it is less than 3 elements left
                    return -1
                # flip 3 elements ig the first element is 0
                for k in range(3):
                    # nums[i+k] ^= 1 #bit manipulaion
                    if nums[i+k] == 0:
                        nums[i+k] = 1
                    else:
                        nums[i+k] = 0
                
                count += 1
        return count


        