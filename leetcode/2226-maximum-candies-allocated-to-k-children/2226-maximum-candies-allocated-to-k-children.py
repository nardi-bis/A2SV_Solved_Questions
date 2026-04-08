class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def checker(mid):
            lijoch = 0
            for pile in candies:
                lijoch += pile // mid
            return lijoch >= k
        
        l = 1
        r = max(candies)

        while l <= r:
            mids = (l + r) // 2
            if checker(mids):
                l = mids + 1
            else:
                r = mids - 1
            
        return r
