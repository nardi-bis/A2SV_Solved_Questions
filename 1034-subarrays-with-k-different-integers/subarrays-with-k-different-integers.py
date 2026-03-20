class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        left1 = left2 = 0
        res = 0
        for right in range(len(nums)):
            count1[nums[right]] += 1
            count2[nums[right]] += 1
            
            while len(count1) > k:
                count1[nums[left1]] -= 1
                if count1[nums[left1]] == 0:
                   del count1[nums[left1]]
                left1 += 1
            while len(count2) > k-1:
                count2[nums[left2]] -= 1
                if count2[nums[left2]] == 0:
                   del count2[nums[left2]]
                left2 += 1
            res += left2 - left1
        return res

        