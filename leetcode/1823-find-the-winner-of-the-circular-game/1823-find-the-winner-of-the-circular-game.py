class Solution:
    def findTheWinner(self, n: int, k: int) -> int: 
        a = [i for i in range(1, n+1)]
        b = 0
        while len(a) > 1:
            b = (b +k-1) % len(a)
            a.pop(b)
        return a[0]
        