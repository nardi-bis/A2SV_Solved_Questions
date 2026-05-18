class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        res = [[capital[i], profits[i]] for i in range(len(profits))]
        res.sort()
        heap = []
        i = 0
        while k > 0:
            while i < len(res) and res[i][0] <= w :
                heapq.heappush(heap, -res[i][1])
                i += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
            k -= 1
        return w
            


