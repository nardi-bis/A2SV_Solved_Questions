class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        eheap = []
        cheap = []
        t = 0
        res = []
        for i, (e,p) in enumerate(tasks):
            heapq.heappush(eheap, (e, p, i))

        while eheap or cheap:
            while eheap and eheap[0][0] <= t:
                e, p , i = heapq.heappop(eheap)
                heapq.heappush(cheap, (p, i))
            if not cheap:
                t = eheap[0][0]
            else:
                p, i = heapq.heappop(cheap)
                res.append(i)
                t += p
        return res


        