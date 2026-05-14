class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap = []
        answer = []
        max_r = 0
        for l, r, h in buildings:
            max_r = max(r, max_r)
        last_l = max_r + 10
        last_r = max_r + 10
        buildings.append([last_l, last_r, 0]) # just for 
        for l, r, h in buildings:
            while heap and heap[0][1] < l:
                hh, rr, ll = heappop(heap)
                while heap and rr >= heap[0][1]:
                    heappop(heap)
                if heap:
                    if heap[0][0] != hh:
                        answer.append([rr, -heap[0][0]])
                else:
                    answer.append([rr, 0])            
            heappush(heap, (-h, r, l))
            if not answer:
                answer.append([l, -heap[0][0]])
            else:
                if l != answer[-1][0] and answer[-1][1] != -heap[0][0]:
                    answer.append([l, -heap[0][0]])
                elif answer[-1][1] != -heap[0][0]:
                    answer[-1][1] = max(answer[-1][1], -heap[0][0])

        return answer