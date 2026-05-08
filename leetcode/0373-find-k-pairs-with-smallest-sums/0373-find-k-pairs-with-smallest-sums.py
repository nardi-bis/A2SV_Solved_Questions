class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        current = []
        res = []
        for i in range(len(nums1)):
            heapq.heappush(current,(nums1[i] + nums2[0],[nums1[i], nums2[0]], (i, 0)))
            # so in this we have (1,2) (7,2) (11, 2) checking all values of nums1 with the smallest     value of nums2
        for _ in range(k):
            su, val, idx = heapq.heappop(current)
            res.append(val)
            i, j = idx
            if j + 1 <= len(nums2) - 1:
                heapq.heappush(current,(nums1[i] + nums2[j + 1],[nums1[i], nums2[j + 1]], (i, j + 1)))
        return res
