class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(mid):
            hrs = 0
            for pile in piles:
                hrs += ceil (pile / mid) 
            return hrs <= h

        l = 1
        r = max(piles)
        
        while l <= r:
            m = (l + r) // 2
            if checker(m):
                r = m - 1
            else:
                l = m + 1
        return l