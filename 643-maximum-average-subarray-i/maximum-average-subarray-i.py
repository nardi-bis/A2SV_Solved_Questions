class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[:k])
        max_ = current_sum
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_=max(max_,current_sum)
           
        return max_/k