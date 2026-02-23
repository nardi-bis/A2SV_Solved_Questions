class Solution:
    def moveZeroes(self, nums):
        holder=0
        seeker=0
        while seeker<len(nums):
            if nums[seeker]!=0:
                nums[seeker],nums[holder]=nums[holder],nums[seeker]
                holder+=1
            seeker+=1
        # first_zero = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0 :
        #         nums[i] , nums[first_zero] = nums[first_zero] ,nums[i]
        #         first_zero += 1
            
        