class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # Only push the first element of each row
        heap = [(matrix[r][0], r, 0) for r in range(n)]
        heapq.heapify(heap)
        
        for _ in range(k - 1):
            val, r, c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
        
        return heapq.heappop(heap)[0]

        