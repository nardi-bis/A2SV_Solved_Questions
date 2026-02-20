class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)//3
        total = 0
        for i in range(len(piles) - 2, n - 1, -2): # start ,stop, step
            total += piles[i]
        return total
