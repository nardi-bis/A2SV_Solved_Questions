class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        res = []
        heap = []
        for i in c.keys():
            heapq.heappush(heap, (-c[i], i))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        