class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)//3
        total = 0
        k = 1
        for _ in range(n): # start ,stop, step
            total += piles[k]
            k += 2
        return total
