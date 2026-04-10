class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def check(dif):
            prev_pos = position[0]
            count = 1
            for i in range(1, len(position)):
                if position[i] - prev_pos >= dif:
                    count += 1
                    prev_pos = position[i]
            return count >= m

        l, r= 1, position[-1] - position[0]

        while l <= r:
            mid = (l + r) // 2
            if check(mid) == True:
                l = mid + 1
            else:
                r = mid - 1

        return r



        