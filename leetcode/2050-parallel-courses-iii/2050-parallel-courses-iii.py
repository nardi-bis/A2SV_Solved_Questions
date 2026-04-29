class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        q = deque()
        for fro, to in relations:
            adj[fro].append(to)
            indeg[to] += 1

        for i in range(1, n + 1):
            if indeg[i] == 0:
                q.append(i)
        month = [0] * (n + 1)
        while q:
            for _ in range(len(q)): # level
                node = q.popleft()
                month[node] += time[node - 1]
                for i in adj[node]: # for the lijs
                    indeg[i] -= 1
                    if indeg[i] == 0:
                        q.append(i)
                    month[i] = max(month[node], month[i])
        return max(month)
                


        