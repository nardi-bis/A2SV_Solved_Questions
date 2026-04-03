class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(capacity):
            cur_day = 1
            sums = 0

            for w in weights:
                sums += w
                if sums > capacity:
                    sums = w
                    cur_day += 1
                    if cur_day > days:
                        return False
            return True

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            if valid(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
            
        

        