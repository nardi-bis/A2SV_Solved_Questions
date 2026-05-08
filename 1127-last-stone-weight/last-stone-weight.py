class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones[-1]
            y = stones[-2]
            stones.pop()
            stones.pop()
            if x != y:
                stones.append(abs(x - y))
        if len(stones) == 1:
            return stones[0]
        return 0


        