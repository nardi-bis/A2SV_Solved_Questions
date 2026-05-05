class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for i in range(n + 1)]
        indeg = [0] * (n + 1)
        for prev, to in relations:
            adj[prev].append(to)
            indeg[to] += 1
        q = deque()

        for i in range(1, n + 1):
            if indeg[i] == 0:
                q.append(i)
        month = [0] * (n + 1)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                month[node] += time[node - 1]
                for child in adj[node]:
                    indeg[child] -= 1
                    month[child] = max(month[node], month[child])
                    if indeg[child] == 0:
                        q.append(child)
        return max(month)


        