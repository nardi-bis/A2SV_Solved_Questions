class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        res = []
        row = len(matrix)
        col = len(matrix[0])
        kth = (row * col) - k
        for r in range(row):
            for c in range(col):
                heapq.heappush(heap, -matrix[r][c])
        for _ in range(kth + 1):
            res.append(heapq.heappop(heap))
        v = res[-1]
        return -v

        